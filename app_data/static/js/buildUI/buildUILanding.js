export function buildHeadline() {
    const mainContainer = document.getElementById('main_container');

    const headlineContainer = document.createElement('div');
    headlineContainer.className = "ml-row";
    headlineContainer.innerHTML = "<h2>Introduction</h2>";

    mainContainer.appendChild(headlineContainer);
}

export async function buildIntroductionText() {
    const url = "/get_introduction_text";

    await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error('Error Introduction Text');
            }
            return response.text();
        }).then(data => {
            const introTextContainer = document.createElement('div');
            introTextContainer.className = "ml-row";
            introTextContainer.id = "introTextContainer";
            introTextContainer.innerHTML = data;

            document.getElementById('main_container').appendChild(introTextContainer);
        }).catch(error => {
            console.error('Error: ', error);
    });

}

export function buildIntroductionQuestionnaire() {
    const questionnaireMainContainer = document.createElement('div');
    questionnaireMainContainer.className = 'row text-center';


    const containerAge = document.createElement('div');
    containerAge.className = 'col-4';
    //containerAge.innerHTML = "<h4 class='text-center'>Age Group</h4>";
    containerAge.innerHTML = "<h4>Age Group</h4>";

    const ageGroups = ["<20", "20-29", "30-39", "40-49", "50-59", "60-69", ">70"];
    containerAge.appendChild(buildDropdown(ageGroups, "Select an age group"));

    questionnaireMainContainer.appendChild(containerAge);


    const containerGender = document.createElement('div');
    containerGender.className = 'col-4';
    containerGender.innerHTML = "<h4>Gender</h4>";

    const genders = ["male", "female", "diverse"];
    containerGender.appendChild(buildDropdown(genders, "Select a gender"));

    questionnaireMainContainer.appendChild(containerGender);


    const containerOccupation = document.createElement('div');
    containerOccupation.className = 'col-4';
    containerOccupation.innerHTML = "<h4>Occupation</h4>";
    questionnaireMainContainer.appendChild(containerOccupation);

    const occupations = ["student", "teacher", "professional", "other", "academic researcher"];
    containerOccupation.appendChild(buildDropdown(occupations, "Select an occupation"));

    document.getElementById('main_container').appendChild(questionnaireMainContainer);

}

function buildDropdown(values, startText) {
    const dropdownContainer = document.createElement('div');
    dropdownContainer.className = "btn-group";

    const dropdownSelect = document.createElement('select');
    dropdownSelect.className = "form-select-lg mb-3";

    let selection = document.createElement('option');
    selection.textContent = startText;
    selection.selected = true;
    selection.value = "none selected";
    dropdownSelect.appendChild(selection);

    values.forEach(value => {
        selection = document.createElement('option');
        selection.textContent = value;
        selection.value = value;
        dropdownSelect.appendChild(selection);
    })

    dropdownContainer.appendChild(dropdownSelect);

    return dropdownContainer;
}

export function buildStartEvaluationPanel() {
    const container = document.createElement('div');
    container.className = "row text-center";

    const subContainer = document.createElement('div');
    subContainer.className = "col";

    const button = document.createElement('button');
    button.className = "btn-lg";
    button.style = "width: 400px;";
    button.type = "button";
    button.textContent = "Start with the evaluation";

    subContainer.appendChild(button);
    container.appendChild(subContainer);

    const text = document.createElement('p');
    text.textContent = "With clicking the 'Start with the evaluation' button you agree that " +
        "your data is collected and used in scientific research!";

    container.appendChild(text);

    document.getElementById('main_container').appendChild(container);
}
