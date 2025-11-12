<script>
	import { login } from '$lib/api';
	import { goto } from '$app/navigation';

	let email = '';
	let password = '';
	let error = '';
	let loading = false;
	let shakeError = false;

	async function handleLogin() {
		error = '';
		loading = true;
		shakeError = false;

		try {
			await login(email, password);
			goto('/dashboard');
		} catch (err) {
			error = err.response?.data?.detail || 'Email o contraseña incorrectos';
			shakeError = true;
			setTimeout(() => {
				shakeError = false;
			}, 500);
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Iniciar Sesión - Wiñay</title>
</svelte:head>

<div class="auth-page-duo">
	<!-- LEFT SIDE - MASCOT & BRANDING -->
	<div class="auth-left">
		<a href="/" class="back-home">
			<span>←</span> Inicio
		</a>

		<div class="mascot-section">
			<div class="mascot-large float-animation">🌱</div>
			<h1>¡Bienvenido de vuelta!</h1>
			<p>Continúa aprendiendo con proyectos reales</p>

			<div class="features-mini">
				<div class="feature-mini">
					<span class="feature-icon">🔥</span>
					<span>Mantén tu racha</span>
				</div>
				<div class="feature-mini">
					<span class="feature-icon">⭐</span>
					<span>Gana más XP</span>
				</div>
				<div class="feature-mini">
					<span class="feature-icon">🏆</span>
					<span>Completa proyectos</span>
				</div>
			</div>
		</div>
	</div>

	<!-- RIGHT SIDE - FORM -->
	<div class="auth-right">
		<div class="auth-form-container" class:shake-animation={shakeError}>
			<h2>Inicia sesión</h2>
			<p class="auth-subtitle">Ingresa tus datos para continuar</p>

			{#if error}
				<div class="error-banner-duo">
					<span class="error-icon-duo">⚠️</span>
					<span>{error}</span>
				</div>
			{/if}

			<form on:submit|preventDefault={handleLogin} class="auth-form-duo">
				<div class="input-group-duo">
					<label for="email">Email</label>
					<input
						id="email"
						type="email"
						bind:value={email}
						placeholder="tu@email.com"
						required
						autocomplete="email"
					/>
				</div>

				<div class="input-group-duo">
					<label for="password">Contraseña</label>
					<input
						id="password"
						type="password"
						bind:value={password}
						placeholder="••••••••"
						required
						autocomplete="current-password"
						minlength="6"
					/>
				</div>

				<button type="submit" class="btn-auth-duo" disabled={loading}>
					{loading ? 'INGRESANDO...' : 'INGRESAR'}
				</button>
			</form>

			<div class="auth-divider">
				<span>o</span>
			</div>

			<p class="auth-switch">
				¿No tienes cuenta?
				<a href="/register">Regístrate gratis</a>
			</p>
		</div>
	</div>
</div>

<style>
	/* AUTH PAGE LAYOUT */
	.auth-page-duo {
		min-height: 100vh;
		display: grid;
		grid-template-columns: 1fr 1fr;
	}

	/* LEFT SIDE - MASCOT */
	.auth-left {
		background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 48px;
		position: relative;
	}

	.back-home {
		position: absolute;
		top: 32px;
		left: 32px;
		display: flex;
		align-items: center;
		gap: 8px;
		color: var(--primary);
		background: white;
		padding: 12px 20px;
		border-radius: var(--radius-full);
		text-decoration: none;
		font-weight: 700;
		font-size: 16px;
		box-shadow: var(--shadow-md);
		transition: all 0.2s;
	}

	.back-home:hover {
		transform: translateX(-4px);
		box-shadow: var(--shadow-lg);
	}

	.mascot-section {
		text-align: center;
		max-width: 500px;
	}

	.mascot-large {
		font-size: 160px;
		margin-bottom: 32px;
		filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.1));
	}

	.auth-left h1 {
		font-size: 48px;
		font-weight: 900;
		color: white;
		margin-bottom: 16px;
		text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.auth-left p {
		font-size: 22px;
		font-weight: 600;
		color: white;
		opacity: 0.95;
		margin-bottom: 48px;
	}

	.features-mini {
		display: flex;
		flex-direction: column;
		gap: 16px;
		align-items: center;
	}

	.feature-mini {
		display: flex;
		align-items: center;
		gap: 12px;
		background: white;
		padding: 12px 24px;
		border-radius: var(--radius-full);
		font-size: 16px;
		font-weight: 700;
		color: var(--gray-900);
		box-shadow: var(--shadow-md);
		min-width: 240px;
	}

	.feature-icon {
		font-size: 24px;
	}

	/* RIGHT SIDE - FORM */
	.auth-right {
		background: white;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 48px;
	}

	.auth-form-container {
		width: 100%;
		max-width: 440px;
	}

	.auth-form-container h2 {
		font-size: 36px;
		font-weight: 800;
		color: var(--gray-900);
		margin-bottom: 8px;
	}

	.auth-subtitle {
		font-size: 18px;
		color: var(--gray-700);
		margin-bottom: 32px;
	}

	/* ERROR BANNER */
	.error-banner-duo {
		display: flex;
		align-items: center;
		gap: 12px;
		background: #FFE5E5;
		border: 2px solid #E63946;
		border-radius: var(--radius-md);
		padding: 16px;
		margin-bottom: 24px;
		font-size: 15px;
		font-weight: 700;
		color: var(--gray-900);
	}

	.error-icon-duo {
		font-size: 20px;
	}

	/* FORM */
	.auth-form-duo {
		display: flex;
		flex-direction: column;
		gap: 20px;
	}

	.input-group-duo {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.input-group-duo label {
		font-size: 16px;
		font-weight: 700;
		color: var(--gray-900);
	}

	.input-group-duo input {
		font-size: 17px;
		padding: 16px;
		border: 2px solid var(--gray-300);
		border-radius: var(--radius-md);
		transition: all 0.2s;
	}

	.input-group-duo input:hover {
		border-color: var(--gray-500);
	}

	.input-group-duo input:focus {
		outline: none;
		border-color: var(--primary);
		box-shadow: 0 0 0 4px var(--primary-light);
	}

	/* BUTTON */
	.btn-auth-duo {
		font-family: 'Nunito', sans-serif;
		font-size: 17px;
		font-weight: 800;
		padding: 18px;
		background: var(--primary);
		color: white;
		border: none;
		border-radius: var(--radius-md);
		text-transform: uppercase;
		letter-spacing: 0.5px;
		cursor: pointer;
		box-shadow: var(--shadow-button);
		border-bottom: 4px solid var(--primary-dark);
		transition: all 0.1s ease;
		margin-top: 8px;
	}

	.btn-auth-duo:hover:not(:disabled) {
		background: var(--primary-hover);
		filter: brightness(1.05);
	}

	.btn-auth-duo:active:not(:disabled) {
		transform: translateY(2px);
		box-shadow: 0 2px 0 var(--primary-dark);
	}

	.btn-auth-duo:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}

	/* DIVIDER */
	.auth-divider {
		text-align: center;
		margin: 32px 0;
		position: relative;
	}

	.auth-divider::before,
	.auth-divider::after {
		content: '';
		position: absolute;
		top: 50%;
		width: 45%;
		height: 2px;
		background: var(--gray-300);
	}

	.auth-divider::before {
		left: 0;
	}

	.auth-divider::after {
		right: 0;
	}

	.auth-divider span {
		background: white;
		padding: 0 16px;
		color: var(--gray-700);
		font-weight: 700;
		font-size: 14px;
		text-transform: uppercase;
	}

	/* SWITCH LINK */
	.auth-switch {
		text-align: center;
		font-size: 16px;
		color: var(--gray-700);
	}

	.auth-switch a {
		color: var(--primary);
		text-decoration: none;
		font-weight: 800;
		margin-left: 4px;
	}

	.auth-switch a:hover {
		text-decoration: underline;
	}

	/* RESPONSIVE */
	@media (max-width: 968px) {
		.auth-page-duo {
			grid-template-columns: 1fr;
		}

		.auth-left {
			display: none;
		}

		.auth-right {
			padding: 32px 24px;
		}

		.auth-form-container h2 {
			font-size: 28px;
		}
	}
</style>
