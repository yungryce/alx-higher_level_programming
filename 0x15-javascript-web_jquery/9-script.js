// JavaScript script that displays the value of hello

$(() => {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, textStatus) => {
      if (textStatus === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  });