$('button').on('click', function(e) {
  $.ajax({
    data: {'b': $(this).attr('id')},
    error: (XMLHttpRequest, textStatus, errorThrown) => {
      alert("エラー:" + errorThrown);
    },
    type: 'POST'
  });
});