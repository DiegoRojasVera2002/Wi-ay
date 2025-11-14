<script>
  let email = "";
  let password = "";
  let error = "";

  // Credenciales hardcodeadas
  const EMPRESA_CREDENTIALS = {
    email: "empresa@bcp.com.pe",
    password: "BCP2024Admin",
  };

  function handleLogin() {
    if (
      email === EMPRESA_CREDENTIALS.email &&
      password === EMPRESA_CREDENTIALS.password
    ) {
      // Login exitoso - guardar en localStorage
      localStorage.setItem("empresaAuth", "true");
      localStorage.setItem("empresaName", "Banco de Crédito del Perú");
      localStorage.setItem("empresaLogo", "/src/logos_empresas/Bcp.png");
      window.location.href = "/empresa/dashboard";
    } else {
      error = "Credenciales incorrectas. Por favor, intenta de nuevo.";
    }
  }
</script>

<svelte:head>
  <title>Login Empresas - Wiñay</title>
</svelte:head>

<div class="login-empresa-page">
  <div class="login-container">
    <!-- Logo y título -->
    <div class="login-header">
      <div class="wiñay-logo">🌱 WIÑAY</div>
      <h1>Portal de Empresas</h1>
      <p class="login-subtitle">Accede a tu panel de reclutamiento</p>
    </div>

    <!-- Credenciales de demostración -->
    <div class="demo-credentials">
      <div class="demo-header">
        <span class="demo-icon">🔑</span>
        <strong>Credenciales de Demo</strong>
      </div>
      <div class="demo-info">
        <p><strong>Email:</strong> empresa@bcp.com.pe</p>
        <p><strong>Contraseña:</strong> BCP2024Admin</p>
      </div>
    </div>

    <!-- Formulario de login -->
    <form on:submit|preventDefault={handleLogin} class="login-form">
      {#if error}
        <div class="error-message">
          <span class="error-icon">⚠️</span>
          {error}
        </div>
      {/if}

      <div class="form-group">
        <label for="email">Email Corporativo</label>
        <input
          type="email"
          id="email"
          bind:value={email}
          placeholder="empresa@tuempresa.com"
          required
        />
      </div>

      <div class="form-group">
        <label for="password">Contraseña</label>
        <input
          type="password"
          id="password"
          bind:value={password}
          placeholder="••••••••"
          required
        />
      </div>

      <button type="submit" class="btn-login-empresa">
        <span>INICIAR SESIÓN</span>
        <span class="arrow">→</span>
      </button>
    </form>

    <!-- Links -->
    <div class="login-footer">
      <a href="/" class="back-link">← Volver al inicio</a>
    </div>
  </div>
</div>

<style>
  .login-empresa-page {
    min-height: 100vh;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
  }

  .login-container {
    background: white;
    border-radius: 24px;
    padding: 48px;
    max-width: 480px;
    width: 100%;
    box-shadow: 0 20px 60px rgba(239, 68, 68, 0.15);
    border: 2px solid #fecaca;
  }

  .login-header {
    text-align: center;
    margin-bottom: 32px;
  }

  .wiñay-logo {
    font-size: 32px;
    font-weight: 900;
    color: #ef4444;
    margin-bottom: 16px;
  }

  .login-header h1 {
    font-size: 32px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 8px;
  }

  .login-subtitle {
    font-size: 16px;
    color: var(--gray-600);
    font-weight: 600;
  }

  .demo-credentials {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border: 2px solid #fbbf24;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 32px;
  }

  .demo-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
    font-size: 16px;
    color: #92400e;
  }

  .demo-icon {
    font-size: 20px;
  }

  .demo-info p {
    font-size: 14px;
    color: #78350f;
    margin: 6px 0;
    font-family: "Monaco", monospace;
  }

  .login-form {
    margin-bottom: 24px;
  }

  .error-message {
    background: #fee2e2;
    border: 2px solid #ef4444;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #991b1b;
    font-weight: 600;
    font-size: 14px;
  }

  .error-icon {
    font-size: 20px;
  }

  .form-group {
    margin-bottom: 24px;
  }

  .form-group label {
    display: block;
    font-weight: 700;
    color: var(--gray-900);
    margin-bottom: 8px;
    font-size: 14px;
  }

  .form-group input {
    width: 100%;
    padding: 14px 16px;
    border: 2px solid var(--gray-300);
    border-radius: 12px;
    font-size: 16px;
    transition: all 0.2s;
    font-family: "Nunito", sans-serif;
  }

  .form-group input:focus {
    outline: none;
    border-color: #ef4444;
    box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
  }

  .btn-login-empresa {
    width: 100%;
    padding: 16px;
    background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.3);
    border-bottom: 4px solid #b91c1c;
  }

  .btn-login-empresa:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
    background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
  }

  .btn-login-empresa:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
  }

  .arrow {
    font-size: 24px;
    font-weight: 900;
  }

  .login-footer {
    text-align: center;
  }

  .back-link {
    color: var(--gray-600);
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s;
  }

  .back-link:hover {
    color: #ef4444;
  }
</style>
