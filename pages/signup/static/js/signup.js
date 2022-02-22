

function signup_validation() {

  if (document.getElementById("number").value.length < 16){
    window.alert("card is not valid.");
    return false;
  }
  return true;
}

