$(document).ready(function() {
  // Toggle password visibility
  $('#toggle-password').on('click', function() {
    $(this).toggleClass('fa-eye-slash');

    const passwordInput = $('#password-input');
    const inputType = passwordInput.attr('type') === 'password' ? 'text' : 'password';
    passwordInput.attr('type', inputType);
  });
});
