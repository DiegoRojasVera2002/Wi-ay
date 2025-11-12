<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { getUser, logout } from '$lib/api';
	import { goto } from '$app/navigation';

	let user = null;
	let showUserMenu = false;

	onMount(() => {
		user = getUser();

		// Close dropdown when clicking outside
		function handleClickOutside(event) {
			if (showUserMenu && !event.target.closest('.user-menu-container')) {
				showUserMenu = false;
			}
		}

		document.addEventListener('click', handleClickOutside);

		return () => {
			document.removeEventListener('click', handleClickOutside);
		};
	});

	function handleLogout() {
		logout();
		user = null;
		showUserMenu = false;
		goto('/');
	}
</script>

<!-- NAVBAR ESTILO DUOLINGO -->
<nav class="nav-duolingo">
	<div class="container nav-content">
		<a href="/" class="logo">
			<div class="logo-circle">🌱</div>
			<span class="logo-text">WIÑAY</span>
		</a>

		<div class="nav-center">
			{#if user}
				<div class="streak-display">
					<span class="streak-flame">🔥</span>
					<span class="streak-number">7</span>
				</div>
				<div class="xp-display">
					<span>⭐</span>
					<span class="xp-number">250 XP</span>
				</div>
			{/if}
		</div>

		<div class="nav-right">
			{#if user}
				<div class="user-menu-container">
					<button class="user-button" on:click={() => showUserMenu = !showUserMenu}>
						<div class="avatar">{user.full_name[0]}</div>
					</button>
					{#if showUserMenu}
						<div class="user-dropdown-duo">
							<div class="dropdown-header">
								<div class="avatar-large">{user.full_name[0]}</div>
								<div>
									<div class="dropdown-name">{user.full_name}</div>
									<div class="dropdown-email">{user.email}</div>
								</div>
							</div>
							<div class="divider"></div>
							<a href="/dashboard" class="dropdown-item-duo">
								📊 Mi Progreso
							</a>
							<a href="/modules" class="dropdown-item-duo">
								📚 Módulos
							</a>
							<a href="/profile" class="dropdown-item-duo">
								⚙️ Configuración
							</a>
							<div class="divider"></div>
							<button class="dropdown-item-duo logout" on:click={handleLogout}>
								🚪 Cerrar Sesión
							</button>
						</div>
					{/if}
				</div>
			{:else}
				<a href="/login" class="btn-secondary">INGRESAR</a>
			{/if}
		</div>
	</div>
</nav>

<slot />

<!-- FOOTER SIMPLE -->
<footer class="footer-duolingo">
	<div class="container">
		<div class="footer-content">
			<div class="footer-left">
				<div class="footer-logo">
					<div class="logo-circle">🌱</div>
					<span>WIÑAY</span>
				</div>
				<p>Aprende haciendo proyectos reales</p>
			</div>
			<div class="footer-links">
				<a href="/about">Sobre Nosotros</a>
				<a href="/modules">Módulos</a>
				<a href="/companies">Para Empresas</a>
				<a href="/help">Ayuda</a>
			</div>
		</div>
		<div class="footer-bottom">
			<p>© 2024 Wiñay. Hecho con ❤️ para estudiantes peruanos.</p>
		</div>
	</div>
</footer>

<style>
	/* NAVBAR DUOLINGO STYLE */
	.nav-duolingo {
		background: white;
		border-bottom: 2px solid var(--gray-300);
		position: sticky;
		top: 0;
		z-index: 1000;
		padding: 12px 0;
	}

	.nav-content {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.logo {
		display: flex;
		align-items: center;
		gap: 12px;
		text-decoration: none;
	}

	.logo-circle {
		width: 48px;
		height: 48px;
		background: linear-gradient(135deg, #FFE5E5 0%, var(--primary) 100%);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 28px;
		border: 3px solid white;
		box-shadow: var(--shadow-md);
	}

	.logo-text {
		font-size: 24px;
		font-weight: 900;
		color: var(--primary);
		letter-spacing: 1px;
	}

	.nav-center {
		display: flex;
		gap: 24px;
		align-items: center;
	}

	.streak-display {
		display: flex;
		align-items: center;
		gap: 8px;
		background: linear-gradient(135deg, #FFA500 0%, #FF6B00 100%);
		color: white;
		padding: 8px 16px;
		border-radius: var(--radius-full);
		font-weight: 800;
		font-size: 18px;
		box-shadow: var(--shadow-sm);
		border: 2px solid white;
	}

	.streak-flame {
		font-size: 22px;
		animation: flame 1.5s ease-in-out infinite;
	}

	.xp-display {
		display: flex;
		align-items: center;
		gap: 8px;
		background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
		color: white;
		padding: 8px 16px;
		border-radius: var(--radius-full);
		font-weight: 800;
		font-size: 16px;
		box-shadow: var(--shadow-sm);
		border: 2px solid white;
	}

	.nav-right {
		display: flex;
		gap: 16px;
		align-items: center;
	}

	.user-menu-container {
		position: relative;
	}

	.user-button {
		background: none;
		border: none;
		padding: 0;
		cursor: pointer;
	}

	.user-button .avatar {
		border: 3px solid var(--primary);
		transition: transform 0.2s;
	}

	.user-button:hover .avatar {
		transform: scale(1.1);
	}

	.user-dropdown-duo {
		position: absolute;
		top: calc(100% + 12px);
		right: 0;
		background: white;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-lg);
		box-shadow: var(--shadow-lg);
		min-width: 280px;
		z-index: 1000;
		overflow: hidden;
	}

	.dropdown-header {
		display: flex;
		gap: 12px;
		padding: 20px;
		background: var(--bg-gray);
		align-items: center;
	}

	.dropdown-name {
		font-weight: 800;
		font-size: 18px;
		color: var(--gray-900);
	}

	.dropdown-email {
		font-size: 14px;
		color: var(--gray-700);
	}

	.dropdown-item-duo {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 16px 20px;
		font-size: 16px;
		font-weight: 700;
		color: var(--gray-900);
		text-decoration: none;
		transition: background 0.2s;
		border: none;
		width: 100%;
		text-align: left;
		cursor: pointer;
		background: white;
	}

	.dropdown-item-duo:hover {
		background: var(--bg-gray);
	}

	.dropdown-item-duo.logout {
		color: var(--primary);
	}

	.dropdown-item-duo.logout:hover {
		background: var(--primary-light);
	}

	/* FOOTER */
	.footer-duolingo {
		background: var(--bg-gray);
		margin-top: 80px;
		padding: 48px 0 24px;
		border-top: 2px solid var(--gray-300);
	}

	.footer-content {
		display: flex;
		justify-content: space-between;
		align-items: start;
		margin-bottom: 32px;
		flex-wrap: wrap;
		gap: 32px;
	}

	.footer-left {
		flex: 1;
	}

	.footer-logo {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 16px;
	}

	.footer-logo span {
		font-size: 20px;
		font-weight: 900;
		color: var(--primary);
	}

	.footer-logo .logo-circle {
		width: 40px;
		height: 40px;
		font-size: 24px;
	}

	.footer-left p {
		color: var(--gray-700);
		font-size: 16px;
	}

	.footer-links {
		display: flex;
		gap: 32px;
		flex-wrap: wrap;
	}

	.footer-links a {
		color: var(--gray-900);
		text-decoration: none;
		font-weight: 700;
		font-size: 16px;
		transition: color 0.2s;
	}

	.footer-links a:hover {
		color: var(--primary);
	}

	.footer-bottom {
		text-align: center;
		padding-top: 24px;
		border-top: 2px solid var(--gray-300);
	}

	.footer-bottom p {
		color: var(--gray-700);
		font-size: 14px;
	}

	@media (max-width: 768px) {
		.nav-center {
			display: none;
		}

		.logo-text {
			display: none;
		}

		.footer-content {
			flex-direction: column;
		}

		.footer-links {
			flex-direction: column;
			gap: 16px;
		}
	}
</style>
