from__future__import print_function

def build_speechlet_response(title,output,reprompt_text, should_end_session):
	return{
		'outputSpeech': {
			'type':'PlainText',
			'text':output
		},
		'card':{
			'type':'Simple',
			'title':'SessionSpeechlet -'+title,
			'content':'SessionSpeechlet -'+output
		},
		'reprompt':{
			'outputSpeech':{
				'type':'PlainText',
				'text':reprompt_text
			}
		},
		'should_end_session':should_end_session

	}

def build_response(session_attributes,speechlet_response):
	return{
		'version':'1.0',
		'sessionAttributes': session_attributes,
		'response':speechlet_response
	}

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def get_welcome_response():
	session_attributes={}
	card_title = "Welcome"
	speech_output = "Welcome to the Job Family Alexa Skill. Please ask me any questions you may have."

	#Generic Response
	reprompt_text = "I'm sorry, I cannot answer your question. Please speak with the regional JF lead."

	should_end_session = False
	return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def handle_seesion_end_request():
	card_title = 'Session Ended'
	speech_output = "See you later"
	should_end_session = True
	return build_response({},build_speechlet_response(card_title, speech_output,None,should_end_session))

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def start_session(start_session_request,session):
	print("start_session requestId=" + start_session_request['requestId']+", sessionId=" + session['sessionId'])



def on_launch(launch_request, session):	
	print("on_launch requestId=" + launch_request['requestId'] + ", sessionId=" +  session['sessionId'])



def on_event(event_request, session):
	print("on_event requestId=" + event_request['requestId'] + ", sessionId=" +  session['sessionId'])

	event = event_request['event']
	event_name = event_request['event']['name']

	#All answers come from here
	if event_name == "JF_Mission":
		return JF_Mission(event, session)
	elif event_name == "JF_Families":
		return JFFamilies(event,session)

