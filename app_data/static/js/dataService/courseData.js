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