$(document).ready(function () {
    // $('#data-table-basic').DataTable();
    $('#data-table-basic').DataTable({
        "order": [[2, "desc"]],
        language: {
            paginate: {
                previous: '&laquo;',
                next: '&raquo;'
            },
            aria: {
                paginate: {
                    previous: 'Previous',
                    next: 'Next'
                }
            }
        }
    });
});
