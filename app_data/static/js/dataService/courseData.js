import {createEvaluationSite} from "../buildUI/buildUIEvaluation.js";

export function getNextCourse() {
    const url = "/get_next_course";

    fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error('Get new course Error');
            }
            return response.json();
        })
        .then(data => {
            createEvaluationSite(data);
        })
        .catch(error => {
            console.error('Error', error);
        });
}

export async function set_choice(course_id, choice) {
    const url = "/set_user_choice"

    const choice_data = {
            "course_id": course_id,
            "user_choice": choice
    }

    await fetch(url, {
        "method": "POST",
        "headers": {
            'Content-Type': 'application/json'
        },
        "body": JSON.stringify(choice_data)
    })
        .then(response => {
            if(!response.ok){
                throw new Error('Set choice error');
            }
        })
        .catch(error => {
            console.error('Error', error);
        });
}
