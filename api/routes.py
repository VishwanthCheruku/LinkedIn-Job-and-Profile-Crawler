from flask import Blueprint, request, jsonify
from models import session, Job, Profile

api_routes = Blueprint('api', __name__)

@api_routes.route('/profiles', methods=['GET'])
def get_profiles():
    designation = request.args.get('designation')
    location = request.args.get('location')
    company = request.args.get('company')
    
    profiles = session.query(Profile).filter(Profile.title.contains(designation)).all()
    return jsonify([profile.__dict__ for profile in profiles[:10]])

@api_routes.route('/jobs', methods=['GET'])
def get_jobs():
    experience = request.args.get('experience')
    job_function = request.args.get('job_function')
    designation = request.args.get('designation')
    location = request.args.get('location')
    
    jobs = session.query(Job).filter(Job.title.contains(designation)).all()
    return jsonify([job.__dict__ for job in jobs[:10]])