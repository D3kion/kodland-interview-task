var prefix = '.kodland__create-post_image',
  input = document.querySelector(prefix + '-input'),
  button = document.querySelector(prefix + '-upload'),
  previewWrapper = document.querySelector(prefix + '-preview-wrapper'),
  preview = document.querySelector(prefix + '-preview'),
  remove = document.querySelector(prefix + '-remove');

button.addEventListener('keydown', function (e) {
  if (e.keyCode == 13 || e.keyCode == 32) input.click();
});
button.addEventListener('click', function (e) {
  e.preventDefault();
  input.click();
});
input.addEventListener('change', function () {
  var file = this.files[0];
  if (!file) return;

  var reader = new FileReader();
  reader.onloadend = function () {
    preview.src = reader.result;
    button.classList.add('hide');
    previewWrapper.classList.remove('hide');
  }
  reader.readAsDataURL(file);
});
remove.addEventListener('click', function (e) {
  e.preventDefault();
  button.classList.remove('hide');
  previewWrapper.classList.add('hide');

  input.files = new DataTransfer().files;
});
