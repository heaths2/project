$(document).ready(function () {
    // $('#data-table-basic').DataTable();
    $('table.display').DataTable({
        "order": [[2, "desc"]],
        "scrollX": true,
        language: {
            "lengthMenu": "페이지당 _MENU_ 개씩 보기",
            "emptyTable": "데이터가 없습니다.",
            "info": "현재 _START_ - _END_ / _TOTAL_ 건",
            "infoEmpty": "현재 0 - 0 / 0 건",
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
