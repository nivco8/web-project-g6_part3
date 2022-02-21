

function signup_validation() {

  if (document.getElementById("password").value != document.getElementById("psw_repeat").value){
    window.alert("password and password repeat are not identical!");
    return false;
  }
  return true;
}

