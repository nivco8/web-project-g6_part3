
function signup_validation() {
  let email = document.forms["sigup"]["email"].value;
  let atposition=email.indexOf("@");
  if (atposition<1){
    alert("Email is not valid");
    return false;
  }
  let phone = document.forms["signUp"]["phone"].value;
  if (phone.length < 10) {
    alert("Phone must contains at least 10 digits");
    return false;
  }
  let address = document.forms["signUp"]["country"].value;
  if (address.includes('Israel') || address.includes('ישראל' )) {
    alert("You must be in an Israeli resident to sign up");
    console.log('TEST')
    return false;
  }
  let password = document.forms["signUp"]["password"].value;
  let psw_repeat = document.forms["signUp"]["psw_repeat"].value;
  if (password != psw_repeat){
    alert("Please repeat is not identical to password");
    console.log('TEST')
    return false;
  }
  return true;
}

