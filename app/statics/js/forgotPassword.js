function resetPassword(form) {
    
    let user = form.elements['user'].value;
    if(user==="")
        return false;
    form.elements[1].disabled = true;
    fetch('/reset-password?user=' + user)
    .then( function(data) { return data.json() })
    .then( function(data){

        let hash = data.hash;
        form.elements[3].setAttribute("type" , "text");
        form.elements[4].setAttribute("type" , "password");
        form.elements[2].value = hash;
        form.elements[5].style.display = "block";

    }) .catch( function(err) { throw err; } )

}
