from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Alexa Skills Kit. " \
                    "Please ask me about Job Families in Credit Suisse"

    reprompt_text = "Please ask me about Job Families"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_intent_attributes(question):
    return {"intent": question}


def job_family_role_intent(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'family' in intent['slots']:
        q = intent['slots']['family']['value']
        session_attributes = create_intent_attributes(q)
        if q == "application architecture & development":
            speech_output = "An AD is responsible for the technical analysis, design, architecture, development, implementation and support of software applications."
        elif q == "business analysis and engineering":
            speech_output = "A BE is responsible for ensuring business requirements are clearly identified, prioritized and satisfied by appropriate technical and or business process solutions."
        elif q == "business management":
            speech_output = "A BM is responsible for supporting the daily operations and controlled activities in running organizations effectively."
        elif q == "it operations":
            speech_output = "A IO is responsible for the deployment and optimization of critical IT infrastructure services."
        elif q == "line management":
            speech_output = "A LM focuses on adopting organization culture change and the effective staff leadership and management competencies that sustain resources."
        elif q == "project management":
            speech_output = "A PM is responsible for initiating, planning, executing, controlling, and closing the work of a team or project to achieve specific goals. "
        elif q == "quality management and testing":
            speech_output = "A QM focuses not only on product and service quality but also how to achieve it in order to achieve consistency. "
        elif q == "service and delivery management":
            speech_output = "A SD is responsible for the delivery of services or service technology to clients."
        elif q == "systems architecture and engineering":
            speech_output = "A SE is responsible for the full lifecycle of technology infrastructure systems globally, including identification of need, sourcing, design, engineering, development, testing, deployments and third level support."
        elif q == "user production and support":
            speech_output = "A UP is responsible for providing all IT support services to clients, maintaining the production environment and working with IT departments to ensure the delivery of requests."
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def job_family_mission_intent(intent, session):
    card_title = 'mission'
    session_attributes = {}
    should_end_session = False
    
    speech_output = "The job family mission is to drive the training curriculum and professionalize the practices and disciplines with cs."
    reprompt_text = "You can ask me what are the job families at cs"
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "JobFamilyRole":
        return job_family_role_intent(intent, session)
    elif intent_name == "JobFamilyMission":
        return job_family_mission_intent(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])


    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
