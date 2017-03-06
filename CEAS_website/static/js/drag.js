$(document).ready(function() {
    //Helper function to keep table row from collapsing when being sorted
    var fixHelperModified = function(e, tr) {
        var $originals = tr.children();
        var $helper = tr.clone();
        $helper.children().each(function(index)
        {
          $(this).width($originals.eq(index).width())
        });
        return $helper;
    };

    //Make diagnosis table sortable
    $("#diagnosis_list tbody").sortable({
        helper: fixHelperModified,
        stop: function(event,ui) {renumber_table('#diagnosis_list')}
    }).disableSelection();

    //Delete button in table rows
    $('table').on('click','.btn-delete',function() {
        tableID = '#' + $(this).closest('table').attr('id');
        r = confirm('Delete this item?');
        if(r) {
            $(this).closest('tr').remove();
            renumber_table(tableID);
            }
    });

    $('table').tablesorter();
});


//Renumber table rows
function renumber_table(tableID) {
    $(tableID + " tr").each(function() {
        count = $(this).parent().children().index($(this)) + 1;
        console.log('s_id'+count);
        $('input[name=change-me]').attr('name','s_id');
        $('input')[1].setAttribute('name','proj_id');
        $('input')[2].setAttribute('name','s_id1');
        $(this).find('.priority').html(count);
    });
}
