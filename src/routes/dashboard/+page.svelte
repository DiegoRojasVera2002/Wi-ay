<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { getUser } from '$lib/api';

	let user = null;

	// Mock data - in real app, this would come from API
	const stats = {
		streak: 7,
		xp: 1240,
		level: 5,
		projectsCompleted: 3,
		projectsInProgress: 2,
		certificates: 1,
		totalProjects: 15
	};

	const achievements = [
		{ icon: '🔥', title: 'Primera Racha', description: '7 días seguidos' },
		{ icon: '⭐', title: 'Primer Proyecto', description: 'Completado' },
		{ icon: '🎯', title: 'Enfocado', description: '5 días activo' },
		{ icon: '🏆', title: 'Campeón', description: 'Top 10%' }
	];

	const recentActivity = [
		{ type: 'project', title: 'Completaste "Sistema de Recomendaciones"', time: 'Hace 2 horas', icon: '✅' },
		{ type: 'xp', title: 'Ganaste 50 XP', time: 'Hace 3 horas', icon: '⭐' },
		{ type: 'streak', title: '¡7 días de racha!', time: 'Hoy', icon: '🔥' }
	];

	onMount(() => {
		user = getUser();
		if (!user) {
			goto('/login');
		}
	});
</script>

<svelte:head>
	<title>Mi Dashboard - Wiñay</title>
</svelte:head>

<div class="dashboard-duo">
	{#if user}
		<div class="container">
			<!-- USER HERO SECTION -->
			<div class="hero-stats-duo">
				<div class="user-profile-duo">
					<div class="avatar-large-duo">{user.full_name[0]}</div>
					<div class="user-info">
						<h1>¡Hola, {user.full_name.split(' ')[0]}!</h1>
						<p>Nivel {stats.level} · {user.university || 'Estudiante'}</p>
					</div>
				</div>

				<div class="key-stats-duo">
					<div class="key-stat streak-stat">
						<div class="stat-icon">🔥</div>
						<div class="stat-content">
							<div class="stat-number">{stats.streak}</div>
							<div class="stat-label">Días de Racha</div>
						</div>
					</div>

					<div class="key-stat xp-stat">
						<div class="stat-icon">⭐</div>
						<div class="stat-content">
							<div class="stat-number">{stats.xp}</div>
							<div class="stat-label">Total XP</div>
						</div>
					</div>

					<div class="key-stat level-stat">
						<div class="stat-icon">🎖️</div>
						<div class="stat-content">
							<div class="stat-number">{stats.level}</div>
							<div class="stat-label">Nivel</div>
						</div>
					</div>
				</div>
			</div>

			<!-- PROGRESS SECTION -->
			<div class="section-title-duo">
				<h2>Tu Progreso</h2>
			</div>

			<div class="progress-grid-duo">
				<div class="progress-card-duo">
					<div class="progress-header">
						<span class="progress-icon">📊</span>
						<h3>Proyectos</h3>
					</div>
					<div class="circular-progress">
						<svg width="140" height="140" viewBox="0 0 140 140">
							<circle cx="70" cy="70" r="60" fill="none" stroke="var(--gray-300)" stroke-width="12" />
							<circle
								cx="70"
								cy="70"
								r="60"
								fill="none"
								stroke="var(--primary)"
								stroke-width="12"
								stroke-linecap="round"
								stroke-dasharray="{(stats.projectsCompleted / stats.totalProjects) * 377} 377"
								transform="rotate(-90 70 70)"
							/>
						</svg>
						<div class="progress-label">
							<div class="progress-value">{stats.projectsCompleted}/{stats.totalProjects}</div>
							<div class="progress-text">Completados</div>
						</div>
					</div>
				</div>

				<div class="progress-card-duo">
					<div class="progress-header">
						<span class="progress-icon">🚀</span>
						<h3>En Curso</h3>
					</div>
					<div class="big-number">{stats.projectsInProgress}</div>
					<p class="progress-desc">Proyectos activos</p>
					<a href="/modules" class="btn-small-duo">CONTINUAR</a>
				</div>

				<div class="progress-card-duo">
					<div class="progress-header">
						<span class="progress-icon">🎓</span>
						<h3>Certificados</h3>
					</div>
					<div class="big-number">{stats.certificates}</div>
					<p class="progress-desc">Certificados obtenidos</p>
					<a href="/certificates" class="btn-small-duo">VER TODOS</a>
				</div>
			</div>

			<!-- ACHIEVEMENTS SECTION -->
			<div class="section-title-duo">
				<h2>Logros</h2>
				<a href="#" class="see-all">Ver todos →</a>
			</div>

			<div class="achievements-grid-duo">
				{#each achievements as achievement}
					<div class="achievement-card-duo">
						<div class="achievement-icon-duo">{achievement.icon}</div>
						<h4>{achievement.title}</h4>
						<p>{achievement.description}</p>
					</div>
				{/each}
			</div>

			<!-- ACTIVITY SECTION -->
			<div class="section-title-duo">
				<h2>Actividad Reciente</h2>
			</div>

			<div class="activity-card-duo">
				{#each recentActivity as activity}
					<div class="activity-item-duo">
						<div class="activity-icon-duo">{activity.icon}</div>
						<div class="activity-content">
							<div class="activity-title">{activity.title}</div>
							<div class="activity-time">{activity.time}</div>
						</div>
					</div>
				{/each}
			</div>

			<!-- QUICK ACTIONS -->
			<div class="section-title-duo">
				<h2>Comienza Ahora</h2>
			</div>

			<div class="quick-actions-duo">
				<a href="/modules" class="action-card-duo">
					<div class="action-icon">📚</div>
					<h3>Explorar Módulos</h3>
					<p>Descubre nuevos proyectos y tecnologías</p>
				</a>

				<a href="/modules" class="action-card-duo">
					<div class="action-icon">💻</div>
					<h3>Continuar Aprendiendo</h3>
					<p>Retoma tu proyecto en curso</p>
				</a>

				<a href="/profile" class="action-card-duo">
					<div class="action-icon">⚙️</div>
					<h3>Configuración</h3>
					<p>Personaliza tu perfil y preferencias</p>
				</a>
			</div>

			<!-- MOTIVATION MASCOT -->
			<div class="motivation-duo">
				<div class="mascot-small float-animation">🌱</div>
				<div class="motivation-text">
					<h3>¡Vas muy bien!</h3>
					<p>Llevas {stats.projectsCompleted} proyectos completados. ¡Sigue así para alcanzar tu meta!</p>
				</div>
			</div>
		</div>
	{/if}
</div>

<style>
	.dashboard-duo {
		min-height: calc(100vh - 80px);
		background: var(--bg);
		padding: 48px 0;
	}

	/* USER HERO */
	.hero-stats-duo {
		background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
		border-radius: var(--radius-xl);
		padding: 40px;
		margin-bottom: 48px;
		box-shadow: var(--shadow-lg);
	}

	.user-profile-duo {
		display: flex;
		align-items: center;
		gap: 24px;
		margin-bottom: 32px;
	}

	.avatar-large-duo {
		width: 80px;
		height: 80px;
		border-radius: 50%;
		background: white;
		color: var(--primary);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 36px;
		font-weight: 800;
		border: 4px solid white;
		box-shadow: var(--shadow-md);
	}

	.user-info h1 {
		font-size: 36px;
		font-weight: 900;
		color: white;
		margin-bottom: 4px;
	}

	.user-info p {
		font-size: 18px;
		font-weight: 700;
		color: white;
		opacity: 0.95;
	}

	/* KEY STATS */
	.key-stats-duo {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
		gap: 20px;
	}

	.key-stat {
		background: white;
		border-radius: var(--radius-lg);
		padding: 20px;
		display: flex;
		align-items: center;
		gap: 16px;
		box-shadow: var(--shadow-md);
		border: 3px solid white;
	}

	.stat-icon {
		font-size: 48px;
	}

	.stat-number {
		font-size: 32px;
		font-weight: 900;
		color: var(--gray-900);
		line-height: 1;
	}

	.stat-label {
		font-size: 14px;
		font-weight: 700;
		color: var(--gray-700);
		text-transform: uppercase;
		letter-spacing: 0.5px;
		margin-top: 4px;
	}

	/* SECTION TITLE */
	.section-title-duo {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 48px 0 24px;
	}

	.section-title-duo h2 {
		font-size: 28px;
		font-weight: 800;
		color: var(--gray-900);
		margin: 0;
	}

	.see-all {
		font-size: 16px;
		font-weight: 700;
		color: var(--primary);
		text-decoration: none;
	}

	.see-all:hover {
		text-decoration: underline;
	}

	/* PROGRESS GRID */
	.progress-grid-duo {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
		gap: 24px;
		margin-bottom: 24px;
	}

	.progress-card-duo {
		background: white;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-lg);
		padding: 28px;
		box-shadow: var(--shadow-md);
		text-align: center;
	}

	.progress-header {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 12px;
		margin-bottom: 20px;
	}

	.progress-icon {
		font-size: 28px;
	}

	.progress-header h3 {
		font-size: 20px;
		font-weight: 800;
		color: var(--gray-900);
		margin: 0;
	}

	/* CIRCULAR PROGRESS */
	.circular-progress {
		position: relative;
		width: 140px;
		height: 140px;
		margin: 0 auto;
	}

	.progress-label {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		text-align: center;
	}

	.progress-value {
		font-size: 24px;
		font-weight: 900;
		color: var(--gray-900);
		line-height: 1;
	}

	.progress-text {
		font-size: 12px;
		font-weight: 700;
		color: var(--gray-700);
		text-transform: uppercase;
		letter-spacing: 0.5px;
		margin-top: 4px;
	}

	.big-number {
		font-size: 56px;
		font-weight: 900;
		color: var(--primary);
		line-height: 1;
		margin: 16px 0;
	}

	.progress-desc {
		font-size: 16px;
		color: var(--gray-700);
		margin-bottom: 16px;
	}

	.btn-small-duo {
		display: inline-block;
		padding: 10px 20px;
		background: var(--primary);
		color: white;
		text-decoration: none;
		border-radius: var(--radius-md);
		font-size: 14px;
		font-weight: 800;
		text-transform: uppercase;
		letter-spacing: 0.5px;
		box-shadow: var(--shadow-sm);
		transition: all 0.2s;
	}

	.btn-small-duo:hover {
		background: var(--primary-hover);
		transform: translateY(-2px);
		box-shadow: var(--shadow-md);
	}

	/* ACHIEVEMENTS */
	.achievements-grid-duo {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
		gap: 20px;
		margin-bottom: 24px;
	}

	.achievement-card-duo {
		background: white;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-lg);
		padding: 24px;
		text-align: center;
		box-shadow: var(--shadow-md);
		transition: all 0.2s;
	}

	.achievement-card-duo:hover {
		transform: translateY(-4px);
		box-shadow: var(--shadow-lg);
	}

	.achievement-icon-duo {
		font-size: 56px;
		margin-bottom: 12px;
	}

	.achievement-card-duo h4 {
		font-size: 18px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 8px;
	}

	.achievement-card-duo p {
		font-size: 14px;
		color: var(--gray-700);
		font-weight: 600;
	}

	/* ACTIVITY */
	.activity-card-duo {
		background: white;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-lg);
		padding: 24px;
		box-shadow: var(--shadow-md);
		margin-bottom: 24px;
	}

	.activity-item-duo {
		display: flex;
		align-items: center;
		gap: 16px;
		padding: 16px;
		border-radius: var(--radius-md);
		transition: background 0.2s;
	}

	.activity-item-duo:hover {
		background: var(--bg-gray);
	}

	.activity-item-duo:not(:last-child) {
		border-bottom: 2px solid var(--gray-300);
	}

	.activity-icon-duo {
		font-size: 32px;
		flex-shrink: 0;
	}

	.activity-content {
		flex: 1;
	}

	.activity-title {
		font-size: 16px;
		font-weight: 700;
		color: var(--gray-900);
		margin-bottom: 4px;
	}

	.activity-time {
		font-size: 14px;
		color: var(--gray-700);
	}

	/* QUICK ACTIONS */
	.quick-actions-duo {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
		gap: 24px;
		margin-bottom: 48px;
	}

	.action-card-duo {
		background: white;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-lg);
		padding: 32px;
		text-decoration: none;
		text-align: center;
		box-shadow: var(--shadow-md);
		transition: all 0.2s;
	}

	.action-card-duo:hover {
		transform: translateY(-4px);
		box-shadow: var(--shadow-lg);
		border-color: var(--primary);
	}

	.action-icon {
		font-size: 56px;
		margin-bottom: 16px;
	}

	.action-card-duo h3 {
		font-size: 20px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 8px;
	}

	.action-card-duo p {
		font-size: 16px;
		color: var(--gray-700);
		line-height: 1.5;
	}

	/* MOTIVATION */
	.motivation-duo {
		background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
		border-radius: var(--radius-xl);
		padding: 32px;
		display: flex;
		align-items: center;
		gap: 24px;
		box-shadow: var(--shadow-lg);
	}

	.mascot-small {
		font-size: 80px;
		flex-shrink: 0;
	}

	.motivation-text h3 {
		font-size: 24px;
		font-weight: 900;
		color: white;
		margin-bottom: 8px;
	}

	.motivation-text p {
		font-size: 18px;
		font-weight: 600;
		color: white;
		opacity: 0.95;
		line-height: 1.5;
	}

	/* RESPONSIVE */
	@media (max-width: 768px) {
		.hero-stats-duo {
			padding: 24px;
		}

		.user-profile-duo {
			flex-direction: column;
			text-align: center;
			margin-bottom: 24px;
		}

		.user-info h1 {
			font-size: 28px;
		}

		.key-stats-duo {
			grid-template-columns: 1fr;
		}

		.section-title-duo {
			flex-direction: column;
			align-items: flex-start;
			gap: 12px;
		}

		.progress-grid-duo {
			grid-template-columns: 1fr;
		}

		.achievements-grid-duo {
			grid-template-columns: repeat(2, 1fr);
		}

		.quick-actions-duo {
			grid-template-columns: 1fr;
		}

		.motivation-duo {
			flex-direction: column;
			text-align: center;
		}
	}
</style>
