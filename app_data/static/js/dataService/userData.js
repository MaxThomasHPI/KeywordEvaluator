export async function createNewUser() {
    const url = "/add_user";

    const ageGroup = document.getElementById('ageGroups').value;
    const gender = document.getElementById('genders').value;
    const occupation = document.getElementById('occupations').value;

    const data = {
            "age_group": ageGroup,
            "gender": gender,
            "occupation": occupation
    };

    await fetch(url, {
        "method": "POST",
        "headers": {
            'Content-Type': 'application/json'
        },
        "body": JSON.stringify(data)
    })
        .then(response => {
            if(!response.ok){
                throw new Error('Sending user data error!');
            }
        })
        .catch(error => {
            console.error('Error', error);
        });
}