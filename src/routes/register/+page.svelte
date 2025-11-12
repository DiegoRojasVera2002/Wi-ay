<script>
	import { register } from '$lib/api';
	import { goto } from '$app/navigation';

	let formData = {
		email: '',
		password: '',
		full_name: '',
		university: '',
		role: 'student'
	};
	let error = '';
	let loading = false;
	let shakeError = false;

	async function handleRegister() {
		error = '';
		loading = true;
		shakeError = false;

		try {
			await register(formData);
			goto('/login');
		} catch (err) {
			error = err.response?.data?.detail || 'Error al crear la cuenta. Intenta de nuevo.';
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
	<title>Registrarse - Wiñay</title>
</svelte:head>

<div class="auth-page-duo">
	<!-- LEFT SIDE - MASCOT & BRANDING -->
	<div class="auth-left">
		<a href="/" class="back-home">
			<span>←</span> Inicio
		</a>

		<div class="mascot-section">
			<div class="mascot-large float-animation">🌱</div>
			<h1>¡Comienza gratis!</h1>
			<p>Aprende tecnología con proyectos reales de empresas</p>

			<div class="features-mini">
				<div class="feature-mini">
					<span class="feature-icon">🚀</span>
					<span>100% gratis siempre</span>
				</div>
				<div class="feature-mini">
					<span class="feature-icon">💼</span>
					<span>Proyectos reales</span>
				</div>
				<div class="feature-mini">
					<span class="feature-icon">🎓</span>
					<span>Certificados avalados</span>
				</div>
			</div>
		</div>
	</div>

	<!-- RIGHT SIDE - FORM -->
	<div class="auth-right">
		<div class="auth-form-container" class:shake-animation={shakeError}>
			<h2>Crea tu cuenta</h2>
			<p class="auth-subtitle">Solo toma 30 segundos</p>

			{#if error}
				<div class="error-banner-duo">
					<span class="error-icon-duo">⚠️</span>
					<span>{error}</span>
				</div>
			{/if}

			<form on:submit|preventDefault={handleRegister} class="auth-form-duo">
				<div class="input-group-duo">
					<label for="full_name">Nombre Completo</label>
					<input
						id="full_name"
						type="text"
						bind:value={formData.full_name}
						placeholder="Juan Pérez"
						required
						autocomplete="name"
					/>
				</div>

				<div class="input-group-duo">
					<label for="email">Email</label>
					<input
						id="email"
						type="email"
						bind:value={formData.email}
						placeholder="tu@email.com"
						required
						autocomplete="email"
					/>
				</div>

				<div class="input-group-duo">
					<label for="university">Universidad (opcional)</label>
					<input
						id="university"
						type="text"
						bind:value={formData.university}
						placeholder="Universidad Nacional..."
						autocomplete="organization"
					/>
				</div>

				<div class="input-group-duo">
					<label for="password">Contraseña</label>
					<input
						id="password"
						type="password"
						bind:value={formData.password}
						placeholder="Mínimo 6 caracteres"
						required
						autocomplete="new-password"
						minlength="6"
					/>
					<span class="input-hint">Usa al menos 6 caracteres</span>
				</div>

				<button type="submit" class="btn-auth-duo" disabled={loading}>
					{loading ? 'CREANDO CUENTA...' : 'CREAR CUENTA'}
				</button>
			</form>

			<div class="auth-divider">
				<span>o</span>
			</div>

			<p class="auth-switch">
				¿Ya tienes cuenta?
				<a href="/login">Inicia sesión</a>
			</p>

			<p class="terms-text">
				Al registrarte, aceptas nuestros Términos de Servicio y Política de Privacidad
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
		overflow-y: auto;
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

	.input-hint {
		font-size: 14px;
		color: var(--gray-700);
		margin-top: -4px;
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
		margin-bottom: 24px;
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

	/* TERMS */
	.terms-text {
		text-align: center;
		font-size: 13px;
		color: var(--gray-700);
		line-height: 1.5;
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
