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
    speech_output = "Welcome to Alexa Best Job Skill. " \
                    "Please ask me about Job Families in Credit Suisse"

    reprompt_text = "Please ask me about Job Families"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Alexa Best Job Skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_intent_attributes(question):
    return {"intent": question}

#JobFamilyFunction Intent
def job_family_function_intent(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'family' in intent['slots']:
        q = intent['slots']['family']['value']
        
        #synonyms
        if intent['slots']['family']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name'] != None:
            q = intent['slots']['family']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "application architecture and development":
            speech_output = "An A.D. is responsible for the technical analysis, design, architecture, development, implementation and support of software applications."
        elif q == "business analysis and engineering":
            speech_output = "A B.E. is responsible for ensuring business requirements are clearly identified, prioritized and satisfied by appropriate technical and or business process solutions."
        elif q == "business management":
            speech_output = "A B.M. is responsible for supporting the daily operations and controlled activities in running organizations effectively."
        elif q == "i.t. operations":
            speech_output = "An I.O. is responsible for the deployment and optimization of critical IT infrastructure services."
        elif q == "line management":
            speech_output = "A L.M. focuses on adopting organization culture change and the effective staff leadership and management competencies that sustain resources."
        elif q == "project management":
            speech_output = "A P.M. is responsible for initiating, planning, executing, controlling, and closing the work of a team or project to achieve specific goals. "
        elif q == "quality management and testing":
            speech_output = "A Q.M. focuses not only on product and service quality but also how to achieve it in order to achieve consistency. "
        elif q == "service and delivery management":
            speech_output = "A S.D. is responsible for the delivery of services or service technology to clients."
        elif q == "systems architecture and engineering":
            speech_output = "A S.E. is responsible for the full lifecycle of technology infrastructure systems globally, including identification of need, sourcing, design, engineering, development, testing, deployments and third level support."
        elif q == "user production and support":
            speech_output = "An U.P. is responsible for providing all IT support services to clients, maintaining the production environment and working with IT departments to ensure the delivery of requests."
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#JobFamilyMission Intent
def job_family_mission_intent(intent, session):
    card_title = 'mission'
    session_attributes = {}
    should_end_session = False
    
    speech_output = "The job family mission is to drive the training curriculum and professionalize the practices and disciplines with cs."
    reprompt_text = "You can ask me what are the job families at cs"
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#JobFamilies Intent
def job_families_intent(intent, session):
    card_title = "families"
    session_attributes = {}
    should_end_session = False

    speech_output = "the 10 job families are application architecture and development.  business analysis and engineering. business management. i.t. operations. line management. project management. quality management and testing. service and delivery management. systems architecture and engineering. user and productions support."
    reprompt_text = "You can ask me what are the job families at cs"
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#JobFamilyFramework Intent
def job_family_framework_intent(intent, session):
    card_title = "framework"
    session_attributes = {}
    should_end_session = False

    speech_output = "The objective is to strengthen the job family framework as a key enabler of career development."
    reprompt_text = "You can ask me what are the job families at cs"
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#CareerTracks Intent
def career_tracks_intent(intent, session):
    card_title = "careertracks"
    session_attributes = {}
    should_end_session = False

    speech_output = "The four career tracks are business management, engineering, production support and solution delivery."
    reprompt_text = "You can ask me what are the job families at cs"
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


#JobFamilyRoles Intent
def job_family_roles_intent(intent, session):

    card_title = 'roles'
    session_attributes = {}
    should_end_session = False

    if 'value' in intent['slots']['family']:
        q = intent['slots']['family']['value']
        
        #synonyms
        if 'values' in intent['slots']['family']['resolutionsPerAuthority'][0]:
            q = intent['slots']['family']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "application architecture and development":
            speech_output = "the roles of an a.d. are development manager. i.t. architect. software engineer. specialist engineer. data engineer."
        elif q == "business analysis and engineering":
            speech_output = "the roles of a b.e. are account or product manager. business analyst. business architect. i.t. strategist. request manager."
        elif q == "business management":
            speech_output = "the roles of the b.m. are administrative assistant. i.t. c.o.o. or chief of staff. i.t. portfolio officer. i.t. vendor management or demand management. risk and controls management. "
        elif q == "i.t. operations":
            speech_output = "the roles of a i.o. are end user operations. infrastructure operations. security operations."
        elif q == "line management":
            speech_output = "the l.m. is aligned with all of the career tracks."
        elif q == "project management":
            speech_output = "the roles of a p.m. are program manager. program management office or p.m.o. project manager."
        elif q == "quality management and testing":
            speech_output = "the roles of a q.m. are quality manager. test engineer. test manager."
        elif q == "service and delivery management":
            speech_output = "the roles of a s.d. are account management. delivery management. service management."
        elif q == "systems architecture and engineering":
            speech_output = "the roles of a s.e. are infrastructure architect. infrastructure engineer. product manager."
        elif q == "user production and support":
            speech_output = "the roles of a u.p. are application support. desktop support. service desk."
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"

    if 'value' in intent['slots']['role']:
        q = intent['slots']['role']['value']
        
        #synonyms
        if 'resolutions' in intent['slots']['role']:
            q = intent['slots']['role']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "software engineer":
            speech_output = "A software engineer needs to analyze problem space, develop models, code, create and maintain documentation, and more."
        elif q == "development manager":
            speech_output = "A development manager needs to identify the drivers, strategies, and needs of clients whiling ensuring cost optimization, is responsible for coordination of cross application dependencies and more. "
        elif q == "i.t. architect":
            speech_output = "An I.T. architect needs to define and maintain architecture, support overall it architecture development and conduct gap analysis as well as other roles."
        elif q == "specialist engineer":
            speech_output = "A specialist engineer needs to be an expert in a given technology or it knowledge area with certain responsibilities such as advisory, analysis, design, implementation and more.  "
        elif q == "data engineer":
            speech_output = "A data engineer covers all data related, define and model and prepare data for analytical or operational uses and may use machine learning, predictive modeling and other responsibilities."
        elif q == "business analyst":
            speech_output = "A business analyst act as a bridge between business and technology, describe processes and propose improvements to process, perform stakeholder analysis as well as other skills."
        elif q == "request manager":
            speech_output = "A request manager define and communicate the request management process and deliverables, responsible for assigning and maintaining business requests and other roles."
        elif q == "business architect":
            speech_output = "A business architect supports the banks I.T. strategy by developing T.O.M.s., work with the business and I.T. to formulate business cases that holistically transition the bank to the target logical and physical design and also understand and manage the effect of change."
        elif q == "i.t. strategist":
            speech_output = "An i.t. strategist delivers a C.S. competitive I.T. strategy that combines the business strategy, be an appreciated advisor to the business divisions and conduct other responsibilities."
        elif q == "account and product manager":
            speech_output = "A A.P.M. define and communicate the product vision and strategic positioning in alignment with credit suisse business and also be responsible for customer and vendor relationship management."
        elif q == "i.t. c.o.o":
            speech_output = "The i.t. c.o.o. is responsible for the overall financial management of the department, talent development, succession planning and promotions and provide governance for third party outsourcing arrangements. "
        elif q == "chief of staff":
            speech_output = "The chief of staff provide support to a department, division, regional or functional head. Plans facilities and issue management and conducts special projects and event planning."
        elif q == "administrative assistant":
            speech_output = "An administrative assistant coordinate and provide office and administrative support to individuals or groups, respond to or follow up on inquiries regarding the units policies and procedures and monitor adherence to health and safety requirements as well as other maintaining and monitoring responsibilities. "
        elif q == "i.t. portfolio officer":
            speech_output = "The i.t. portfolio officer own and manage i.t. product, leverage relationships, own it portfolio management governance, and much much more."
        elif q == "i.t. vendor management":
            speech_output = "The demand management or i.t. vendor management is responsible for defining best practices for managing outsourcing arrangements, support SVM in negotiation preparation and forecast and track I.T. capital expenditure."
        elif q == "risk and controls management":
            speech_output = "The risk and controls management provides ongoing services to ensure operational risk compliance, manage a program of work to ensure compliance with operational risk policies and monitor and report if needed any compliance status."
        elif q == "infrastructure operator":
            speech_output = "Infrastructure operators deploy and administer infrastructure components such as servers, manages change configuration capacity and lifecycle management, ensure compliance to R.T.O., R.P.O. and availability requirements."
        elif q == "end user operator":
            speech_output = "End User operators deploy and administer as messaging, collaboration and mobile applications, ensure compliance and archive emails/I.M.S./voice messages."
        elif q == "security operator":
            speech_output = "As a security operator, one must deploy and administer security infrastructure components, both physical and software while monitoring the escalation of security events and conduct forensic investigation. "
        elif q == "line manager":
            speech_output = "A line manager are responsible for strategic change delivery, operational management, business partner relationship and human capital management."
        elif q == "project manager":
            speech_output = "A project manager manages, plans, organizes and implements one or more i.t. Projects using standard methodology. "
        elif q == "project management office":
            speech_output = "A p.m.o provides support for financials tracking and change request management while also supporting stakeholder and business client management."
        elif q == "test manager":
            speech_output = " A test manager plan, coordinate and control the entire test process within one or more projects. They also are responsible for managing, implementing and monitoring all test efforts while also ensuring all activities met with guidelines and are compliant with rules and regulations."
        elif q == "test engineer":
            speech_output = "A test engineer execute testing inline with the test strategy and approach and are there to support the test manager to ensure all requested technical facilitation are setup as defined in the test plan."
        elif q == "quality manager":
            speech_output = "A quality manager proposes and define quality objectives to meet customer needs and required product quality as well as contribute to quality management and quality improvement initiatives and ensure all management is compliant with c.s. Standards and policies. "
        elif q == "account manager":
            speech_output = "The account manager are in charge with owning the account portfolio and ensuring an appropriate balance between clients and the i.t. Supplier concerns, explain service, cost metrics and related trends to clients."
        elif q == "delivery manager":
            speech_output = "A delivery manager manage the delivery of i.t. Infrastructure or application development solutions, ensure a clear understanding of client objectives as well as plan and coordinate and ensure timely and on-budget delivery."
        elif q == "service manager":
            speech_output = "The service manager manages an individual or group of i.t. Services and the achievement of respective s.l.a.s. They work and partner with all internal and external service providers to ensure that the i.t. Services are continuously delivered and accurately reported."
        elif q == "product manager":
            speech_output = "A product manager provide the market mind-set required for the outcome based definition of services, build a detailed understanding of customer and user requirements, drive continuous improvement for products and balance change and innovation."
        elif q == "infrastructure architect":
            speech_output = "The infrastructure architect define the strategy and architecture for a technology domains, define the long term strategy and target architecture and drive innovation by exploring and testing new technologies that drive value."
        elif q == "service desk":
            speech_output = "The service desk act as a single point of contact, log all incoming calls to the service desk, contribute to the knowledge base and input to major incident process."
        elif q == "desktop support":
            speech_output = "A desktop support communicate request and incident status to relevant stakeholders, monitors progress of ticket in accordance with defined service level agreements and more."
        elif q == "application support":
            speech_output = "The application support analyze incident and problem trends and propose proactive measures to improve stability and improve efficiency, while also managing vendor relationships and act as single point of contact for all escalated operational service delivery issues."
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#JobBelong Intent
def job_belong_intent(intent, session):

    card_title = 'belong'
    session_attributes = {}
    should_end_session = False

    if 'role' in intent['slots']:
        q = intent['slots']['role']['value']
        
        #synonyms
        if intent['slots']['role']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name'] != None:
            q = intent['slots']['role']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "development manager" or q == "i.t. architect" or q == "software engineer" or q == "specialist engineer" or q == "data engineer":
            speech_output = q + " belongs to a.d. or application architecture and development"
        elif q == "account or product manager" or q == "business analyst" or q == "business architect" or q == "i.t. strategist" or q == "request manager":
            speech_output = q + " belongs to b.e. or business analysis and engineering"
        elif q == "administrative assistant" or q == "i.t. c.o.o." or q == "chief of staff" or q == "i.t. portfolio officer" or q == "i.t. vendor management" or "risk and controls management":
            speech_output = q + " belongs to b.m. or business management"
        elif q == "end user operations" or q == "infrastructure operations" or q == "security operatoins":
            speech_output = q + " belongs to i.o. or i.t. operations"
        elif q == "program manager" or q == "program management office" or q == "project manager":
            speech_output = q + " belongs to p.m. or project management"
        elif q == "quality manager" or q == "test engineer" or q == "test manager":
            speech_output = q + " belongs to q.m. or quality management"
        elif q == "account management" or q == "delivery management" or q == "service management":
            speech_output = q + " belongs to s.d. or service and delivery management"
        elif q == "infrastructure architect" or q == "infrastructure engineer" or q == "product manager":
            speech_output = q + " belongs to s.e. or systems architecture and engineering"
        elif q == "application support" or q == "desktop support" or q == "service desk":
            speech_output = q + " belongs to u.p. or user production and support"
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#TrackJobFamilies Intent
def track_job_families_intent(intent, session):
    card_title = 'track'
    session_attributes = {}
    should_end_session = False

    if 'track' in intent['slots']:
        q = intent['slots']['track']['value']
        
        #synonyms
        if intent['slots']['track']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name'] != None:
            q = intent['slots']['track']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "engineering":
            speech_output = "The job families of engineering track are application architecture and development, systems architecture, and engineering."
        elif q == "production support":
            speech_output = "The job families of production support are i.t. operations, and user and production support."
        elif q == "solution delivery":
            speech_output = "The job families of solution delivery are business analysis and engieering, project management, quality management and testing, and service delivery and management."
        elif q == "business management":
            speech_output = "The job familiy of business management is business management."
        else:
            speech_output = "I'm not sure what you're asking"
        reprompt_text = "You can ask me what are the job families at cs"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#JobCert Intent
def job_cert_intent(intent, session):

    card_title = 'cert'
    session_attributes = {}
    should_end_session = False

    if 'family' in intent['slots']:
        q = intent['slots']['family']['value']
        
        #synonyms
        if intent['slots']['family']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name'] != None:
            q = intent['slots']['family']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
            
        session_attributes = create_intent_attributes(q)
        
        if q == "application architecture and development":
            speech_output = "Some certificates that an a.d. Can receive is the b.c.s.f.l.s.d or the o.r.a.j.s.e.7. Or the i.e.e.e.c.s.d.p.."
        elif q == "business analysis and engineering":
            speech_output = "Some certificates that an b.e. Can receive are the c.b.a.p.. The C.b.i.p.. The b.c.s.f."
        elif q == "business management":
            speech_output = "The certificates that a b.m. can receive are the c.p.a. Or the a.c.c.a.. As well as the e.b.."
        elif q == "project management":
            speech_output = "The certificates that a p.m.. can gain range from the c.a..p.m to the p.r.i.2.p.."
        elif q == "quality management and testing":
            speech_output = "The certificates that a q.m. can receive are the s.q.e., the s.a.q.e.o.q. And also the i.s.t.q.b.e.x.p.."
        else:
            speech_output = "Try asking me about certificates for a.d., b.e., b.m., q.m, or p.m."
        reprompt_text = "You can ask me what are the job families at cs"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def jf_extra_help(intent, session):
	card_title = 'Resources'
	session_attributes = {}
	should_end_session = False
	speech_output = "Recommendations for further education include: coursera, khan academy, codecademy, udemy, udacity, and edx."
	reprompt_text = "you can also ask me what has remained the same"
	
	return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def jf_frame_change(intent, session):
	card_title = 'changes'
	session_attributes = {}
	should_end_session = False

	speech_output = "the updates to the frameworks include now the four career tracks, an industry-aligned roles, framework of skills with three proficiency levels and training opportunities."
	reprompt_text = "you can also ask me what has remained the same"
	
	return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def jf_frame_unchange(intent, session):
	card_title = 'same'
	session_attributes = {}
	should_end_session = False

	speech_output = "the parts of the framework that will stay the same are the 10 job families, the corporate titles, global and regional job family heads and the job family will be visible in the hr system. "
	reprompt_text = "you can also ask me what has changed about the framework"
	
	return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def jf_training_contacts(intent, session):
	card_title = 'contacts'
	session_attributes = {}
	should_end_session = False

	speech_output = "The regional training partners that you can talk to are Zara Shortte who is the head of the e.m.e.a. Region. Eva Zeron who is in charge of the Americas. Arvind Sahu and Rahman Shanawas who both oversee the Asia-Pacific region. Finally there is Silvio Rutsche who oversee Switzerland. Please talk to one of our Regional Job Family Leads to receive their emails and telephone numbers."
	reprompt_text = "please visit my friendly leads here to collect any information to reach these contacts."
	
	return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def jf_value_staff(intent, session):
	card_title = 'staff'
	session_attributes = {}
	should_end_session = False

	speech_output = "the value proposition and use cases for staff are used to find relevant training opportunities.identify your skill gaps and transferable skills. and much more."

	reprompt_text = "You can also ask how it helps out the managers"
	
	return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def jf_value_manager(intent, session):
	card_title = 'managers'
	session_attributes = {}
	should_end_session = False

	speech_output = "the value proposition and use cases for managers are used to help an employee in your team formulate their p.d.p.. Provide clarity on skills you expect from your staff and much more."
	reprompt_text = "You can also ask how it helps out the staff"
	
	return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def jf_count(intent, session):
    card_title = 'familycount'
    session_attributes = {}
    should_end_session = False
    speech_output = "the ten job families are application architecture and development.  business analysis and engineering. business management. i t operations. line management. project management. quality management and testing. service and delivery management. systems architecture and engineering. user and productions support."
    reprompt_text = "Count"
	
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def general_response():
    card_titile = "gen"
    session_attributes = {}
    should_end_session = False
    speech_output = "I am sorry, I am unable to provide an answer to your question. Please visit one of our regional job family leads that are present here at the expo to acquire a possible answer."
    reprompt_text = "generic"
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
    if intent_name == "JobFamilyFunction":
        return job_family_function_intent(intent, session)
    elif intent_name == "JobFamilyMission":
        return job_family_mission_intent(intent, session)
    elif intent_name == "JobFamilies":
        return job_families_intent(intent, session)
    elif intent_name == "JobFamilyFramework":
        return job_family_framework_intent(intent, session)
    elif intent_name == "CareerTracks":
        return career_tracks_intent(intent, session)
    elif intent_name == "JobFamilyRoles":
        return job_family_roles_intent(intent, session)
    elif intent_name == "JobBelong":
        return job_belong_intent(intent, session)
    elif intent_name == "TrackJobFamilies":
        return track_job_families_intent(intent, session)
    elif intent_name == "JobCert":
        return job_cert_intent(intent, session)
    elif intent_name == "JFExtraHelp":
        return jf_extra_help(intent, session)
    elif intent_name == "JFFrameChange":
        return jf_frame_change(intent, session)
    elif intent_name == "JFFrameUnchange":
        return jf_frame_unchange(intent, session)
    elif intent_name == "JFTrainingContacts":
        return jf_training_contacts(intent, session)
    elif intent_name == "JFValueStaff":
        return jf_value_staff(intent, session)
    elif intent_name == "JFValueManager":
        return jf_value_manager(intent, session)
    elif intent_name == "JFCount":
        return jf_count(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        return general_response()


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
