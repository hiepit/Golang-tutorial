    def button_adjust_inventory(self):
        """
            - Get raw data from excel file
            - From raw data, create values for I.
            - Create Product from these values.
        """
        _logger.info('>>>>>> START Adjust Inventory<<<<<<')
        self.ensure_one()
        if not self.file_import:
            raise UserError(_('Please attach import file!'))

        header_indexes, data_products = self.read_excel_file()
        data_len_per_job = 1000
        data_of_jobs = self.split_data(data_products, data_len_per_job)
        queue_jobs = self.env['queue.job']
        for data in data_of_jobs:
            from_index = data[0][-1]
            to_index = data[-1][-1]
            description = _(
                "Inventory adjustment: %d lines from line %d to %d line.") % (
                    to_index - from_index + 1, from_index, to_index)
            delayed_job = self.with_delay(
                description=description).adjust_inventory(
                data, header_indexes, from_index, to_index)
            job = queue_jobs.search(
                [("uuid", "=", delayed_job.uuid)], limit=1)
            if job:
                queue_jobs |= job
        if queue_jobs:
            return {
                'domain': [('id', 'in', queue_jobs.ids)],
                'name': _('Queue jobs to adjust inventory'),
                'view_mode': 'tree,form',
                'res_model': 'queue.job',
                'type': 'ir.actions.act_window'
            }
        _logger.info('>>>>>> END Adjust Inventory<<<<<<')
