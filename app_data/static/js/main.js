import {buildHeadline, buildIntroductionText, buildIntroductionQuestionnaire, buildStartEvaluationPanel} from "./buildUI/buildUILanding.js";

async function setUpLandingPage() {
    await buildHeadline();

    await buildIntroductionText();

    await buildIntroductionQuestionnaire();

    await buildStartEvaluationPanel();
}



document.addEventListener("DOMContentLoaded", setUpLandingPage);
