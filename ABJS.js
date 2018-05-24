const Alexa = require('alexa-sdk');

///////////////////////////////////////
const skillName = "Job Family";
//////////////////////////////////////
const JFMasterList = {
	''
}

function JFMission(){
	const missionAnswer = "The Job Family mission is to drive the training curriculum and professionalize the practices and disciplines with CS";

	this.response.cardRender(skillName, missionAnswer);
	this.response.speak(speechOutput);
	this.emit(':responseReady');
}

function JFMission(){
	const missionAnswer = "The Job Family mission is to drive the training curriculum and professionalize the practices and disciplines with CS";
	
	this.response.cardRender(skillName, missionAnswer);
	this.response.speak(speechOutput);
	this.emit(':responseReady');
}