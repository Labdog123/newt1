
function user_id(){
      x = document.getElementById('id_first_name').value;
      y = document.getElementById('id_last_name').value;
      document.getElementById('id_username').innerHTML = x +' '+ y;
}
user_id();