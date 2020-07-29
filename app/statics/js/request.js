const validate_offer = (id) => {
    console.log(id);
    fetch('/admin/details/' + id + '/valid')
        .then(function(response) {
            
        }, function(error) {
            console.log("Error!" + error)
        }
    )
}