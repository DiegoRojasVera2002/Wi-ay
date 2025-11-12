import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const api = axios.create({
	baseURL: API_URL
});

// Auth
export const login = async (email, password) => {
	const response = await api.post('/auth/login', { email, password });
	if (response.data.access_token) {
		localStorage.setItem('token', response.data.access_token);
		localStorage.setItem('user', JSON.stringify(response.data.user));
	}
	return response.data;
};

export const register = async (userData) => {
	const response = await api.post('/auth/register', userData);
	return response.data;
};

export const logout = () => {
	localStorage.removeItem('token');
	localStorage.removeItem('user');
};

export const getUser = () => {
	const user = localStorage.getItem('user');
	return user ? JSON.parse(user) : null;
};

// Modules
export const getModules = async () => {
	const response = await api.get('/modules');
	return response.data;
};

export const getModuleProjects = async (moduleId) => {
	const response = await api.get(`/modules/${moduleId}/projects`);
	return response.data;
};

// Projects
export const getProject = async (projectId) => {
	const response = await api.get(`/projects/${projectId}`);
	return response.data;
};

export const getProjectSteps = async (projectId) => {
	const response = await api.get(`/projects/${projectId}/steps`);
	return response.data;
};

export const enrollInProject = async (projectId, userId) => {
	const response = await api.post('/projects/enroll', { project_id: projectId }, {
		params: { user_id: userId }
	});
	return response.data;
};

// Submissions
export const submitCode = async (stepId, code, userId) => {
	const response = await api.post('/submissions/submit', {
		step_id: stepId,
		code,
		language: 'python'
	}, {
		params: { user_id: userId }
	});
	return response.data;
};
