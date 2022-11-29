/***************************************Industry Knowledge Start Hear******************************************/
$(document).ready(function () {
    var clonedSoftSkillRow = $('.soft-skill-row').clone(true, true).append('<span class="remove-soft-skill-row glyphicon glyphicon-trash"></span>');
   $('.add-anoter-softskill').on('click', function (e) {
       if($(this).hasClass("add-soft")){
           $(this).closest('.soft-skill-category').find('.soft-skill-row').last().after($(clonedSoftSkillRow).clone(true, true));
           generateSoftSkillsRow('soft-skill-row', this);
       }
   });
});

$(document).on('click', '.remove-soft-skill-row',function (e) {
   if($(this).closest(".row").hasClass("soft-skill-row")){
       $(this).parent().remove();
       var deletedRowId = $(this).parent().data('row');
       reassignSoftSkillId('soft-skill-row');
   }
});

function generateSoftSkillsRow(thisClass, thisVal) {
   var rowCount = $(thisVal).closest(".soft-skill-category").find("."+thisClass).length;
   $(thisVal).closest(".soft-skill-category").find("."+thisClass).each(function(i,v){
       $(this).removeAttr('class').addClass('row mb10 text-italic '+thisClass+' '+thisClass+'-' + (i + 1));
       $(this).attr('data-row',(i+1));
   });
   /* Adding dynamic id's to select picker based on row*/
   $(thisVal).closest(".soft-skill-category").find('.'+thisClass+':eq('+ (rowCount-1) +') .selectpicker').each(function (index, val) {
       var selectId = $(val).attr('id');
       selectId = selectId +'_'+ rowCount;
       $(val).attr('id', selectId);
   });

   /* Initializing the select picker */
   $(thisVal).closest(".soft-skill-category").find('.'+thisClass+':eq('+ (rowCount-1) +') .selectpicker').selectpicker();
}

function reassignSoftSkillId(thisVal){
   var rowCount = $('.'+ thisVal).length;
   console.log(rowCount);
   $('.'+thisVal).each(function(index, val){
       var self_id=index+1;
       $(this).removeAttr('class').addClass('row mb10 text-italic '+thisVal+' '+thisVal+'-' + self_id);
       $(this).attr('data-row', self_id);
       $(val).children().each(function(index2, val2){
           var id = $(val2).find('select').data('id');
           id = id + '_' + self_id;
           $(val2).find('select').attr('id', id).selectpicker('refresh');
           $(val2).find('.bs-placeholder').data('id', id);
       });
   });
}

/***************************************Industry Knowledge End Hear******************************************/

$(document).ready(function () {
    var clonedSoftCategoryRow = $('.soft-skill-category').clone(true, true).append('<span class="remove-skill-category-row glyphicon glyphicon-trash"></span>');
   $('.add-anoter-value-cat').on('click', function (e) {
    if($(this).hasClass("add-category")){
        $(this).closest('.add-soft-skills').find('.soft-skill-category').last().after($(clonedSoftCategoryRow).clone(true, true));
        generateSoftskillCategory('soft-skill-category');
    }
});
});

$(document).on('click', '.remove-skill-category-row',function (e) {
    if($(this).closest(".row").hasClass("soft-skill-category")){
        $(this).parent().remove();
        var deletedRowId = $(this).parent().data('row');
        reassignSoftIdCategory('soft-skill-category');
    }
 });

 function generateSoftskillCategory(thisVal) {
    //alert(thisVal);
    var rowCount = $('.'+thisVal).length;
    $('.'+thisVal).each(function(i,v){
        $(this).removeAttr('class').addClass('row mb10 text-italic '+thisVal+' '+thisVal+'-' + (i + 1));
        $(this).attr('data-row',(i+1));
    });
    /* Adding dynamic id's to select picker based on row*/
    $('.'+thisVal+':eq('+ (rowCount-1) +') .selectpicker').each(function (index, val) {
        var selectId = $(val).attr('id');
        selectId = selectId +'_'+ rowCount;
        $(val).attr('id', selectId);
    });
    /* Initializing the select picker */
    $('.'+thisVal+':eq('+ (rowCount-1) +') .selectpicker').selectpicker();
 }

 function reassignSoftIdCategory(thisVal){
    var rowCount = $('.'+ thisVal).length;
    console.log(rowCount);
    $('.'+thisVal).each(function(index, val){
        var self_id=index+1;
        $(this).removeAttr('class').addClass('row mb10 text-italic '+thisVal+' '+thisVal+'-' + self_id);
        $(this).attr('data-row', self_id);
        $(val).children().each(function(index2, val2){
            var id = $(val2).find('select').data('id');
            id = id + '_' + self_id;
            $(val2).find('select').attr('id', id).selectpicker('refresh');
            $(val2).find('.bs-placeholder').data('id', id);
        });
    });
 }