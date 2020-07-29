const validate_offer = (id) => {
    console.log(id);
    fetch('/admin/details/' + id + '/valid')
        .then(function(response) {
            
        }, function(error) {
            console.log("Error!" + error)
        }
    )
}

const reject_offer = (id) => {
    console.log(id);
    fetch('/admin/details/' + id + '/invalid')
        .then(function(response) {
            
        }, function(error) {
            console.log("Error!" + error)
        }
    )
}

const remove_offer = (id) => {
    console.log(id);
    fetch('/admin/details/' + id + '/remove')
        .then(function(response) {
            
        }, function(error) {
            console.log("Error!" + error)
        }
    )
}