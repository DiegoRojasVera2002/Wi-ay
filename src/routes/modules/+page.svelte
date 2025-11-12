<script>
	import { onMount } from 'svelte';
	import { getModules } from '$lib/api';
	import { getUser } from '$lib/api';

	let modules = [];
	let loading = true;
	let user = null;

	onMount(async () => {
		try {
			user = getUser();
			modules = await getModules();
		} catch (error) {
			console.error('Error loading modules:', error);
		} finally {
			loading = false;
		}
	});

	const moduleIcons = {
		'Data Science': '📊',
		'IoT': '🔌',
		'Web Development': '💻',
		'Fintech': '💰'
	};

	// Simulate progress for demo (in real app, this would come from API)
	function getModuleProgress(index) {
		if (index === 0) return { completed: 3, total: 5, status: 'in-progress' };
		if (index === 1) return { completed: 0, total: 4, status: 'locked' };
		if (index === 2) return { completed: 0, total: 6, status: 'locked' };
		return { completed: 0, total: 4, status: 'locked' };
	}
</script>

<svelte:head>
	<title>Módulos - Wiñay</title>
</svelte:head>

<div class="modules-page-duo">
	<!-- HEADER SIMPLE -->
	<div class="header-duo">
		<div class="container">
			<h1>¡Tu ruta de aprendizaje!</h1>
			<p class="subtitle">Completa proyectos reales y avanza en tu carrera tech</p>
		</div>
	</div>

	<!-- LEARNING PATH - DUOLINGO STYLE -->
	<div class="container">
		{#if loading}
			<div class="loading-duo">
				<div class="loading-spinner">🔄</div>
				<p>Cargando tu ruta...</p>
			</div>
		{:else if modules.length === 0}
			<div class="empty-state-duo">
				<div class="empty-mascot">🌱</div>
				<h3>¡Pronto habrá módulos increíbles!</h3>
				<p>Estamos preparando proyectos reales para ti</p>
			</div>
		{:else}
			<div class="learning-path">
				<div class="path-container">
					{#each modules as module, index}
						{@const progress = getModuleProgress(index)}
						{@const position = index % 2 === 0 ? 'left' : 'right'}

						<div class="path-node {position}" class:locked={progress.status === 'locked'}>
							<!-- Connecting line (except for first) -->
							{#if index > 0}
								<div class="path-line"></div>
							{/if}

							<!-- Module Node -->
							<a
								href={progress.status === 'locked' ? '#' : `/modules/${module.id}`}
								class="module-node-duo"
								class:locked={progress.status === 'locked'}
								class:in-progress={progress.status === 'in-progress'}
								class:completed={progress.status === 'completed'}
							>
								<!-- Progress ring -->
								<svg class="progress-ring" width="140" height="140">
									<circle
										class="progress-ring-bg"
										cx="70"
										cy="70"
										r="62"
									/>
									<circle
										class="progress-ring-fill"
										cx="70"
										cy="70"
										r="62"
										style="stroke-dasharray: {(progress.completed / progress.total) * 389} 389;"
									/>
								</svg>

								<!-- Icon and content -->
								<div class="node-content">
									<div class="node-icon">
										{progress.status === 'locked' ? '🔒' : moduleIcons[module.category] || '📚'}
									</div>
								</div>

								<!-- Lock overlay -->
								{#if progress.status === 'locked'}
									<div class="lock-overlay">
										<div class="lock-icon">🔒</div>
									</div>
								{/if}
							</a>

							<!-- Module info -->
							<div class="module-info-duo">
								<h3 class="module-title-duo">{module.title}</h3>
								<p class="module-desc-duo">{module.description}</p>

								<!-- Progress badge -->
								<div class="progress-badge-duo">
									{#if progress.status === 'locked'}
										<span class="badge-locked">Bloqueado</span>
									{:else if progress.status === 'completed'}
										<span class="badge-completed">✓ Completado</span>
									{:else}
										<span class="badge-progress">{progress.completed}/{progress.total} proyectos</span>
									{/if}
								</div>

								<!-- Start button -->
								{#if progress.status !== 'locked'}
									<a href="/modules/{module.id}" class="btn-start-duo">
										{progress.status === 'completed' ? 'REVISAR' : 'CONTINUAR'}
									</a>
								{/if}
							</div>
						</div>

						<!-- Star decoration between nodes -->
						{#if index < modules.length - 1}
							<div class="path-star">⭐</div>
						{/if}
					{/each}

					<!-- Mascot at the end -->
					<div class="path-mascot">
						<div class="mascot-circle-path">🌱</div>
						<p class="mascot-text">¡Sigue así! Cada proyecto te acerca más a tu meta</p>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	.modules-page-duo {
		min-height: calc(100vh - 80px);
		background: var(--bg);
		padding-bottom: 80px;
	}

	/* HEADER */
	.header-duo {
		padding: 48px 0 32px;
		text-align: center;
	}

	.header-duo h1 {
		font-size: 42px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 8px;
	}

	.subtitle {
		font-size: 20px;
		color: var(--gray-700);
		font-weight: 600;
	}

	/* LOADING */
	.loading-duo {
		text-align: center;
		padding: 80px 20px;
	}

	.loading-spinner {
		font-size: 48px;
		animation: spin 1s linear infinite;
	}

	@keyframes spin {
		from { transform: rotate(0deg); }
		to { transform: rotate(360deg); }
	}

	.loading-duo p {
		margin-top: 16px;
		font-size: 18px;
		color: var(--gray-700);
		font-weight: 700;
	}

	/* EMPTY STATE */
	.empty-state-duo {
		text-align: center;
		padding: 80px 20px;
		max-width: 500px;
		margin: 0 auto;
	}

	.empty-mascot {
		font-size: 80px;
		margin-bottom: 24px;
		animation: float 3s ease-in-out infinite;
	}

	.empty-state-duo h3 {
		font-size: 28px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 12px;
	}

	.empty-state-duo p {
		font-size: 18px;
		color: var(--gray-700);
	}

	/* LEARNING PATH - DUOLINGO STYLE */
	.learning-path {
		max-width: 600px;
		margin: 0 auto;
		position: relative;
	}

	.path-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 32px;
		padding: 40px 0;
	}

	.path-node {
		display: flex;
		align-items: center;
		gap: 32px;
		width: 100%;
		position: relative;
	}

	.path-node.left {
		flex-direction: row;
	}

	.path-node.right {
		flex-direction: row-reverse;
	}

	/* Connecting line */
	.path-line {
		position: absolute;
		top: -32px;
		left: 50%;
		transform: translateX(-50%);
		width: 4px;
		height: 32px;
		background: var(--gray-300);
	}

	/* MODULE NODE (CIRCULAR) */
	.module-node-duo {
		width: 140px;
		height: 140px;
		border-radius: 50%;
		background: white;
		border: 4px solid var(--primary);
		box-shadow: var(--shadow-lg);
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
		cursor: pointer;
		transition: all 0.3s;
		flex-shrink: 0;
		text-decoration: none;
	}

	.module-node-duo:hover:not(.locked) {
		transform: scale(1.1);
		box-shadow: 0 8px 0 rgba(0, 0, 0, 0.15);
	}

	.module-node-duo:active:not(.locked) {
		transform: scale(1.05);
	}

	.module-node-duo.locked {
		border-color: var(--gray-400);
		background: var(--gray-100);
		cursor: not-allowed;
	}

	.module-node-duo.in-progress {
		border-color: var(--primary);
		animation: pulse 2s ease-in-out infinite;
	}

	.module-node-duo.completed {
		border-color: var(--primary);
		background: var(--primary-light);
	}

	/* Progress ring */
	.progress-ring {
		position: absolute;
		top: -4px;
		left: -4px;
		transform: rotate(-90deg);
	}

	.progress-ring-bg {
		fill: none;
		stroke: var(--gray-300);
		stroke-width: 4;
	}

	.progress-ring-fill {
		fill: none;
		stroke: var(--primary);
		stroke-width: 6;
		stroke-linecap: round;
		transition: stroke-dasharray 0.6s ease;
	}

	.module-node-duo.locked .progress-ring-fill {
		stroke: var(--gray-400);
	}

	/* Node content */
	.node-content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		z-index: 1;
	}

	.node-icon {
		font-size: 52px;
	}

	/* Lock overlay */
	.lock-overlay {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(255, 255, 255, 0.9);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.lock-icon {
		font-size: 36px;
		opacity: 0.6;
	}

	/* MODULE INFO */
	.module-info-duo {
		flex: 1;
		min-width: 0;
	}

	.path-node.left .module-info-duo {
		text-align: left;
	}

	.path-node.right .module-info-duo {
		text-align: right;
	}

	.module-title-duo {
		font-size: 24px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 8px;
	}

	.module-desc-duo {
		font-size: 16px;
		color: var(--gray-700);
		margin-bottom: 12px;
		line-height: 1.5;
	}

	/* Progress badge */
	.progress-badge-duo {
		margin-bottom: 16px;
	}

	.progress-badge-duo span {
		display: inline-block;
		padding: 6px 14px;
		border-radius: var(--radius-full);
		font-size: 14px;
		font-weight: 800;
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.badge-locked {
		background: var(--gray-300);
		color: var(--gray-700);
	}

	.badge-completed {
		background: var(--primary-light);
		color: var(--primary);
	}

	.badge-progress {
		background: var(--primary-light);
		color: var(--primary);
	}

	/* Start button */
	.btn-start-duo {
		display: inline-flex;
		align-items: center;
		padding: 12px 24px;
		background: var(--primary);
		color: white;
		text-decoration: none;
		border-radius: var(--radius-md);
		font-weight: 800;
		font-size: 16px;
		text-transform: uppercase;
		letter-spacing: 0.5px;
		box-shadow: var(--shadow-button);
		border-bottom: 4px solid var(--primary-dark);
		transition: all 0.1s ease;
	}

	.btn-start-duo:hover {
		background: var(--primary-hover);
		filter: brightness(1.05);
	}

	.btn-start-duo:active {
		transform: translateY(2px);
		box-shadow: 0 2px 0 var(--primary-dark);
	}

	/* Star decoration */
	.path-star {
		font-size: 32px;
		animation: twinkle 2s ease-in-out infinite;
	}

	@keyframes twinkle {
		0%, 100% { opacity: 1; transform: scale(1); }
		50% { opacity: 0.5; transform: scale(0.9); }
	}

	/* Mascot at end */
	.path-mascot {
		text-align: center;
		margin-top: 48px;
	}

	.mascot-circle-path {
		width: 100px;
		height: 100px;
		background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
		border-radius: 50%;
		display: inline-flex;
		align-items: center;
		justify-content: center;
		font-size: 56px;
		border: 4px solid white;
		box-shadow: var(--shadow-lg);
		margin-bottom: 16px;
		animation: float 3s ease-in-out infinite;
	}

	.mascot-text {
		font-size: 18px;
		font-weight: 700;
		color: var(--gray-700);
		max-width: 400px;
		margin: 0 auto;
	}

	/* RESPONSIVE */
	@media (max-width: 768px) {
		.header-duo h1 {
			font-size: 32px;
		}

		.subtitle {
			font-size: 18px;
		}

		.path-node {
			flex-direction: column !important;
			text-align: center;
		}

		.path-node.right .module-info-duo {
			text-align: center;
		}

		.module-node-duo {
			width: 120px;
			height: 120px;
		}

		.progress-ring {
			width: 120px;
			height: 120px;
		}

		.node-icon {
			font-size: 44px;
		}

		.module-title-duo {
			font-size: 20px;
		}

		.module-desc-duo {
			font-size: 14px;
		}
	}
</style>
