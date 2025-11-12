<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { getModuleProjects } from '$lib/api';

	let moduleId;
	let projects = [];
	let loading = true;
	let error = null;

	$: moduleId = $page.params.id;

	onMount(async () => {
		try {
			projects = await getModuleProjects(moduleId);
		} catch (err) {
			error = 'Error cargando los proyectos';
			console.error(err);
		} finally {
			loading = false;
		}
	});

	const difficultyColors = {
		'beginner': '#10b981',
		'intermediate': '#f59e0b',
		'advanced': '#ef4444'
	};

	const difficultyLabels = {
		'beginner': 'Principiante',
		'intermediate': 'Intermedio',
		'advanced': 'Avanzado'
	};
</script>

<svelte:head>
	<title>Módulo - Wiñay</title>
</svelte:head>

<div class="module-page">
	<div class="container">
		<div class="back-link">
			<a href="/modules">← Volver a Módulos</a>
		</div>

		{#if loading}
			<div class="loading">Cargando proyectos...</div>
		{:else if error}
			<div class="error-message card">{error}</div>
		{:else if projects.length === 0}
			<div class="empty-state card">
				<h3>No hay proyectos en este módulo aún</h3>
			</div>
		{:else}
			<div class="module-header">
				<h1>Proyectos del Módulo</h1>
				<p>Elige un proyecto para comenzar tu aprendizaje</p>
			</div>

			<div class="projects-list">
				{#each projects as project}
					<div class="project-card card">
						<div class="project-header">
							<div>
								<div class="project-order">Proyecto {project.order}</div>
								<h3>{project.title}</h3>
							</div>
							<div
								class="difficulty-badge"
								style="background: {difficultyColors[project.difficulty] || '#6b7280'};"
							>
								{difficultyLabels[project.difficulty] || project.difficulty}
							</div>
						</div>

						<p class="project-description">{project.description}</p>

						<div class="project-footer">
							<div class="company">
								<span class="company-icon">🏢</span>
								Propuesto por: <strong>{project.company_name}</strong>
							</div>
							<a href="/projects/{project.id}" class="btn-primary">
								Comenzar Proyecto →
							</a>
						</div>
					</div>
				{/each}
			</div>
		{/if}
	</div>
</div>

<style>
	.module-page {
		min-height: calc(100vh - 80px);
		padding: 2rem 0 4rem;
	}

	.back-link {
		margin-bottom: 2rem;
	}

	.back-link a {
		color: var(--primary);
		text-decoration: none;
		font-weight: 500;
		transition: opacity 0.2s;
	}

	.back-link a:hover {
		opacity: 0.8;
	}

	.module-header {
		text-align: center;
		margin-bottom: 3rem;
	}

	.module-header p {
		color: var(--text-light);
		font-size: 1.125rem;
		margin-top: 0.5rem;
	}

	.loading {
		text-align: center;
		padding: 3rem;
		color: var(--text-light);
	}

	.error-message {
		text-align: center;
		padding: 2rem;
		color: var(--danger);
	}

	.empty-state {
		text-align: center;
		padding: 3rem;
	}

	.projects-list {
		display: flex;
		flex-direction: column;
		gap: 2rem;
		max-width: 900px;
		margin: 0 auto;
	}

	.project-card {
		transition: all 0.3s;
	}

	.project-card:hover {
		transform: translateY(-2px);
		box-shadow: 0 8px 16px rgba(0,0,0,0.1);
	}

	.project-header {
		display: flex;
		justify-content: space-between;
		align-items: start;
		margin-bottom: 1rem;
		gap: 1rem;
	}

	.project-order {
		color: var(--primary);
		font-size: 0.875rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.project-card h3 {
		margin: 0.25rem 0 0;
	}

	.difficulty-badge {
		padding: 0.375rem 0.875rem;
		border-radius: 20px;
		color: white;
		font-size: 0.875rem;
		font-weight: 600;
		white-space: nowrap;
	}

	.project-description {
		color: var(--text-light);
		line-height: 1.6;
		margin: 1rem 0;
	}

	.project-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-top: 1.5rem;
		padding-top: 1.5rem;
		border-top: 1px solid var(--border);
		flex-wrap: wrap;
		gap: 1rem;
	}

	.company {
		color: var(--text-light);
		font-size: 0.9375rem;
	}

	.company-icon {
		margin-right: 0.25rem;
	}

	.company strong {
		color: var(--text);
	}
</style>
