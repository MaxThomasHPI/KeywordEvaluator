import {getNextCourse, set_choice} from "../dataService/courseData.js";

let course_id;

function clearContainer(container) {

    while (container.firstChild){
        container.removeChild(container.firstChild);
    }
}

export function createEvaluationSite(courseData){
    course_id = courseData.courseID;

    const mainContainer = document.getElementById('main_container');

    clearContainer(mainContainer);

    mainContainer.appendChild(buildTitle(courseData));
    mainContainer.appendChild(buildDescriptionText(courseData));
    mainContainer.appendChild(buildKeywordLists(courseData));
}

function buildTitle(courseData){
    const titleRow = document.createElement('div');
    titleRow.className = 'ml-row';
    titleRow.innerHTML = `<h2>${courseData.title}</h2>`;

    return titleRow;
}

function buildDescriptionText(courseData) {
    const container = document.createElement('div');
    container.className = "ml-row";

    const subContainer = document.createElement('div');
    subContainer.className = 'col';
    container.appendChild(subContainer);

    const text = document.createElement('p');

    if(courseData.description){
        text.innerHTML = courseData.description;
    } else {
        text.innerHTML = "This course has no description available. The keywords are only based " +
            "on the course title";
    }

    subContainer.appendChild(text);

    return container;
}

function buildKeywordLists(courseData) {
    const container = document.createElement('div');
    container.className = "row";

    const tags = ["gen", "man"];

    const left_index = Math.floor(Math.random()*2);
    let right_index;

    if(left_index === 0){
        right_index = 1;
    }else{
        right_index = 0;
    }

    container.appendChild(buildKeywordList(courseData[tags[left_index]], tags[left_index]));
    container.appendChild(buildKeywordList(courseData[tags[right_index]], tags[right_index]));

    return container;
}

function buildKeywordList(keywords, tag) {
    const container = document.createElement('div');
    container.className = "col-6";

    const keywordsList = document.createElement('ol');
    container.appendChild(keywordsList);

    keywords.forEach(keyword => {
        const element = document.createElement('li');
        element.textContent = keyword;
        keywordsList.appendChild(element);
    });

    const buttonContainer = document.createElement('div');
    buttonContainer.className = 'text-center';
    container.appendChild(buttonContainer)

    const choiceButton = document.createElement('button');
    choiceButton.className = 'btn-lg';
    choiceButton.textContent = "This list is better!";
    choiceButton.id = tag;
    choiceButton.onclick = function () {
        set_choice_and_move_on(tag);
    }

    buttonContainer.appendChild(choiceButton);

    return container;
}

function set_choice_and_move_on(tag) {
    set_choice(course_id, tag);
    getNextCourse();
}

export function buildFinished() {
    const container = document.getElementById('main_container');

    clearContainer(container);

    const headlineContainer = document.createElement('div');
    headlineContainer.className = 'ml-row';
    const headline = document.createElement('p');
    headline.innerHTML = '<h2>End of survey</h2>';
    headlineContainer.appendChild(headline);

    container.appendChild(headlineContainer);


    const textContainer = document.createElement('div');
    textContainer.className = 'ml-row';
    const text = document.createElement('p');
    text.innerHTML = 'Thank you for participating in the keyword evaluation! <br>' +
        'You can now close the browser. Your answers have been saved.'
    textContainer.appendChild(text);

    container.appendChild(textContainer);
}