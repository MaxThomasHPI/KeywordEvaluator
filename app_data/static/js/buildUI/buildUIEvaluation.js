function clearContainer(container) {

    if(container.childNodes){
        container.childNodes.forEach(node => {
            container.removeChild(node);
        });
    }
}

export function createEvaluationSite(courseData){
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

    const tags = ["genKeywords", "manKeywords"]

    const left_index = Math.floor(Math.random()*2);
    let right_index;

    if(left_index === 0){
        right_index = 1;
    }else{
        right_index = 0;
    }

    container.appendChild(buildKeywordList(courseData[tags[left_index]], left_index));
    container.appendChild(buildKeywordList(courseData[tags[right_index]], right_index));

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

    buttonContainer.appendChild(choiceButton);

    return container;
}

