import {createEvaluationSite} from "../buildUI/buildUIEvaluation.js";

const courseData = {
    "courseID": 1,
    "title": "Test_Course",
    "description": "This is the description text for a test course.",
    "genKeywords": ["gen_Keyword1", "gen_Keyword2", "gen_Keyword3", "gen_Keyword4"],
    "manKeywords": ["man_Keyword1", "man_Keyword2", "man_Keyword3"]
};

createEvaluationSite(courseData);
