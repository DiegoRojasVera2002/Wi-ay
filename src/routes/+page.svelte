<script>
  import { onMount } from "svelte";
  import lottie from "lottie-web";

  onMount(() => {
    // Animación 1: Coding
    lottie.loadAnimation({
      container: document.getElementById("lottie-coding"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json", // Coding animation
    });

    // Animación 2: Success/Trophy
    lottie.loadAnimation({
      container: document.getElementById("lottie-trophy"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets9.lottiefiles.com/packages/lf20_touohxv0.json", // Trophy animation
    });

    // Animación 3: Personalized
    lottie.loadAnimation({
      container: document.getElementById("lottie-personalized"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets1.lottiefiles.com/packages/lf20_v1yudlrx.json", // Personalized animation
    });

    // Animación 4: Team/Community
    lottie.loadAnimation({
      container: document.getElementById("lottie-team"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets5.lottiefiles.com/packages/lf20_myejiggj.json", // Team animation
    });

    // Animación 5: Business
    lottie.loadAnimation({
      container: document.getElementById("lottie-business"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets8.lottiefiles.com/packages/lf20_k0M4I3.json", // Business animation
    });

    // Animación 6: Certificate
    lottie.loadAnimation({
      container: document.getElementById("lottie-certificate"),
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: "https://assets1.lottiefiles.com/packages/lf20_tll0j4bb.json", // Certificate animation
    });
  });
</script>

<svelte:head>
  <title>Wiñay - La mejor forma de aprender tecnología</title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
  />
</svelte:head>

<!-- HERO - Igual a Duolingo -->
<section class="hero-duo">
  <div class="container hero-container">
    <div class="hero-left">
      <h1>La forma gratis, divertida y efectiva de aprender tecnología</h1>
      <div class="hero-badges">
        <div class="badge-duo">
          <span class="badge-icon">🏆</span>
          <span>Efectivo</span>
        </div>
        <div class="badge-duo">
          <span class="badge-icon">🎮</span>
          <span>Divertido</span>
        </div>
        <div class="badge-duo">
          <span class="badge-icon">💯</span>
          <span>Gratis</span>
        </div>
      </div>
      <a href="/register" class="btn-hero">COMIENZA GRATIS</a>
      <a href="/login" class="link-hero">YA TENGO UNA CUENTA</a>
      <a href="/empresa/login" class="btn-empresa-hero">
        <span class="empresa-icon">🏢</span>
        SOY UNA EMPRESA
      </a>
    </div>
    <div class="hero-right">
      <!-- svelte-ignore a11y-img-redundant-alt -->
      <img
        src="src/gif/original-2e51736906dcaf4c009f77942f20b59a.gif"
        alt="Animated image of learning"
        class="hero-gif"
      />
    </div>
  </div>
</section>

<!-- POR QUÉ WIÑAY - DISEÑO ESPECTACULAR -->
<section class="why-section">
  <!-- Patrón de fondo con iconos educativos -->
  <div class="icon-pattern">
    <i class="fas fa-graduation-cap"></i>
    <i class="fas fa-book"></i>
    <i class="fas fa-laptop-code"></i>
    <i class="fas fa-trophy"></i>
    <i class="fas fa-chart-line"></i>
    <i class="fas fa-lightbulb"></i>
    <i class="fas fa-certificate"></i>
    <i class="fas fa-brain"></i>
    <i class="fas fa-users"></i>
    <i class="fas fa-rocket"></i>
    <i class="fas fa-star"></i>
    <i class="fas fa-code"></i>
    <i class="fas fa-flask"></i>
    <i class="fas fa-pen-fancy"></i>
    <i class="fas fa-globe"></i>
    <i class="fas fa-book-open"></i>
    <i class="fas fa-chalkboard-teacher"></i>
    <i class="fas fa-microscope"></i>
    <i class="fas fa-calculator"></i>
    <i class="fas fa-atom"></i>
    <i class="fas fa-graduation-cap"></i>
    <i class="fas fa-book"></i>
    <i class="fas fa-laptop-code"></i>
    <i class="fas fa-trophy"></i>
    <i class="fas fa-chart-line"></i>
    <i class="fas fa-lightbulb"></i>
    <i class="fas fa-certificate"></i>
    <i class="fas fa-brain"></i>
    <i class="fas fa-users"></i>
    <i class="fas fa-rocket"></i>
    <i class="fas fa-star"></i>
    <i class="fas fa-code"></i>
    <i class="fas fa-flask"></i>
    <i class="fas fa-pen-fancy"></i>
    <i class="fas fa-globe"></i>
    <i class="fas fa-book-open"></i>
    <i class="fas fa-chalkboard-teacher"></i>
    <i class="fas fa-microscope"></i>
    <i class="fas fa-calculator"></i>
    <i class="fas fa-atom"></i>
  </div>

  <div class="container">
    <h2 class="text-center">Por qué Wiñay funciona</h2>
    <p class="why-subtitle">
      Combinamos ciencia del aprendizaje con tecnología de punta
    </p>

    <!-- GRID 3 COLUMNAS UNIFORME -->
    <div class="features-grid-zigzag">
      <!-- Feature 1: Efectivo -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-coding" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">📚</div>
        <h3>Efectivo y comprobado</h3>
        <p>
          Completar proyectos en Wiñay equivale a un semestre universitario
          completo de aprendizaje práctico.
        </p>
      </div>

      <!-- Feature 2: Personalizado -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-personalized" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">🎯</div>
        <h3>Personalizado para ti</h3>
        <p>
          Proyectos que se adaptan a tu nivel. Aprende a tu propio ritmo, cuando
          y donde quieras.
        </p>
      </div>

      <!-- Feature 3: Motivación -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-trophy" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">🔥</div>
        <h3>Mantén tu motivación</h3>
        <p>
          Sistema de rachas, logros y recompensas que hace que aprender sea
          adictivo y divertido.
        </p>
      </div>

      <!-- Feature 4: Certificados -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-certificate" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">🎓</div>
        <h3>Certificados avalados</h3>
        <p>
          Construye un portafolio profesional con certificados validados por
          empresas reales.
        </p>
      </div>

      <!-- Feature 5: Comunidad -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-team" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">👥</div>
        <h3>Comunidad activa</h3>
        <p>
          Más de 1,200 estudiantes peruanos aprendiendo juntos. Comparte y crece
          con otros.
        </p>
      </div>

      <!-- Feature 6: Empresas -->
      <div class="feature-card">
        <div class="feature-visual">
          <div id="lottie-business" class="lottie-compact"></div>
        </div>
        <div class="feature-icon-compact">💼</div>
        <h3>Conecta con empresas</h3>
        <p>
          Completa proyectos reales y accede a oportunidades laborales
          exclusivas.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- STATS - Mejoradas -->
<section class="stats-duo">
  <div class="container text-center">
    <h2>Más de 1,200 estudiantes confían en Wiñay</h2>
    <p class="stats-subtitle">Números que hablan por sí solos</p>
    <div class="stats-grid-duo">
      <div class="stat-duo">
        <div class="stat-icon-duo">📚</div>
        <div class="stat-number-duo">1,200+</div>
        <div class="stat-label-duo">Estudiantes activos</div>
        <div class="stat-trend">↑ 23% este mes</div>
      </div>
      <div class="stat-duo">
        <div class="stat-icon-duo">🚀</div>
        <div class="stat-number-duo">45</div>
        <div class="stat-label-duo">Proyectos reales</div>
        <div class="stat-trend">+5 nuevos</div>
      </div>
      <div class="stat-duo">
        <div class="stat-icon-duo">🏢</div>
        <div class="stat-number-duo">28</div>
        <div class="stat-label-duo">Empresas partner</div>
        <div class="stat-trend">↑ 8 últimas semanas</div>
      </div>
      <div class="stat-duo">
        <div class="stat-icon-duo">🎓</div>
        <div class="stat-number-duo">892</div>
        <div class="stat-label-duo">Certificados emitidos</div>
        <div class="stat-trend">↑ 156 esta semana</div>
      </div>
    </div>
  </div>
</section>

<!-- EMPRESAS QUE CONFÍAN EN NOSOTROS -->
<section class="companies-section">
  <div class="container">
    <div class="companies-header">
      <h2 class="companies-title">Empresas que confían en Wiñay</h2>
      <p class="companies-subtitle">
        Nuestros estudiantes trabajan con las mejores empresas del Perú
      </p>
    </div>
    <div class="companies-grid">
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Bcp.png"
          alt="BCP"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/interbank.png"
          alt="Interbank"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Pagoseguro.png"
          alt="PagoSeguro"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Agrodata.png"
          alt="AgroData"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Innovabank.png"
          alt="InnovaBank"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Mercadope.png"
          alt="MercadoPe"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Logitrack.png"
          alt="LogiTrack"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Mediapp.png"
          alt="MediApp"
          class="company-logo-img"
        />
      </div>
      <div class="company-logo-card">
        <img
          src="/src/logos_empresas/Prestatech.png"
          alt="PrestaTech"
          class="company-logo-img"
        />
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="testimonials-duo">
  <div class="container">
    <h2 class="text-center">Lo que dicen nuestros estudiantes</h2>
    <p class="testi-subtitle">Historias reales de éxito</p>
    <div class="testimonials-grid">
      <div class="testimonial-duo">
        <div class="testimonial-header">
          <div class="avatar-large">
            <img
              src="src/avatars/sarai-alejandro.jpeg"
              alt="Avatar of María González"
              class="avatar-large"
            />
          </div>
          <div>
            <div class="testi-name">Sarai Alejandro</div>
            <div class="testi-uni">UNI</div>
          </div>
        </div>
        <p class="testi-text">
          "Gracias a Wiñay conseguí mi primera práctica en una startup tech. Los
          proyectos reales me dieron la experiencia que necesitaba."
        </p>
        <div class="testi-badge">
          <span>🎓</span> Certificado en Detección de Fraude
        </div>
      </div>

      <div class="testimonial-duo">
        <div class="testimonial-header">
          <div class="avatar-large">
            <img
              src="src/avatars/marcelo-castro.png"
              alt="Avatar of Marcelo Ferre"
              class="avatar-large"
            />
          </div>
          <div>
            <div class="testi-name">Marcelo Ferre</div>
            <div class="testi-uni">PUCP</div>
          </div>
        </div>
        <p class="testi-text">
          "Aprendí Data Science desde cero. Ahora trabajo como Data Analyst en
          una fintech. Wiñay cambió mi vida."
        </p>
        <div class="testi-badge">
          <span>🎓</span> Certificado en Segmentación de Clientes
        </div>
      </div>

      <div class="testimonial-duo">
        <div class="testimonial-header">
          <div class="avatar-large">
            <img
              src="src/avatars/sebastian-lizarraga.png"
              alt="Avatar of Sebastian Lizarraga"
              class="avatar-large"
            />
          </div>
          <div>
            <div class="testi-name">Sebastian Lizarraga</div>
            <div class="testi-uni">UNI</div>
          </div>
        </div>
        <p class="testi-text">
          "Los proyectos de IoT me prepararon para el mercado laboral real. El
          mejor recurso para estudiantes peruanos."
        </p>
        <div class="testi-badge">
          <span>🎓</span> Certificado en Dashboard IoT
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA FINAL -->
<section class="cta-duo">
  <div class="container cta-container">
    <div class="mascot-cta float-animation">🌱</div>
    <h2>Comienza tu camino hacia el éxito tech</h2>
    <p>Únete gratis y empieza a aprender hoy mismo</p>
    <a href="/register" class="btn-hero">COMIENZA AHORA</a>
  </div>
</section>

<style>
  /* HERO */
  .hero-duo {
    background: white;
    padding: 80px 0 60px;
    min-height: 600px;
    display: flex;
    align-items: center;
  }

  .hero-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
  }

  .hero-left h1 {
    font-size: 48px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 32px;
    line-height: 1.1;
  }

  .hero-badges {
    display: flex;
    gap: 16px;
    margin-bottom: 32px;
    flex-wrap: wrap;
  }

  .badge-duo {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: var(--bg-gray);
    border-radius: var(--radius-full);
    border: 2px solid var(--gray-300);
    font-weight: 700;
    color: var(--gray-900);
  }

  .badge-icon {
    font-size: 24px;
  }

  .btn-hero {
    display: inline-block;
    background: var(--primary);
    color: white;
    padding: 20px 48px;
    border-radius: var(--radius-full);
    font-size: 19px;
    font-weight: 800;
    text-transform: uppercase;
    text-decoration: none;
    box-shadow: 0 6px 0 var(--primary-dark);
    transition: all 0.1s;
    letter-spacing: 1px;
    margin-bottom: 16px;
  }

  .btn-hero:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 0 var(--primary-dark);
  }

  .btn-hero:active {
    transform: translateY(2px);
    box-shadow: 0 4px 0 var(--primary-dark);
  }

  .link-hero {
    display: block;
    color: var(--primary);
    font-weight: 800;
    font-size: 16px;
    text-transform: uppercase;
    text-decoration: none;
    letter-spacing: 1px;
    margin-top: 16px;
  }

  .link-hero:hover {
    text-decoration: underline;
  }

  .btn-empresa-hero {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin-top: 24px;
    padding: 14px 32px;
    background: linear-gradient(135deg, #fb923c 0%, #f97316 100%);
    color: white;
    border-radius: var(--radius-full);
    font-size: 15px;
    font-weight: 800;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
    border: 3px solid transparent;
  }

  .btn-empresa-hero:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.4);
    background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%);
  }

  .empresa-icon {
    font-size: 18px;
  }

  .hero-right {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .hero-gif {
    width: 600px;
    height: 600px;
    object-fit: contain;
    filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.1));
  }

  /* WHY SECTION - DISEÑO ROJO ESPECTACULAR */
  .why-section {
    background: var(--primary);
    padding: 80px 20px;
    position: relative;
    overflow: hidden;
  }

  /* Patrón de iconos educativos */
  .icon-pattern {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(5, 1fr);
    gap: 80px;
    padding: 60px;
    padding-top: 250px;
    z-index: 1;
    opacity: 0.35;
  }

  .icon-pattern i {
    color: #ffffff;
    font-size: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: iconFloat 6s ease-in-out infinite;
    animation-delay: calc(var(--icon-index, 0) * 0.2s);
    filter: drop-shadow(0 2px 8px rgba(255, 255, 255, 0.3));
  }

  .icon-pattern i:nth-child(1) {
    --icon-index: 0;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(2) {
    --icon-index: 1;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(3) {
    --icon-index: 2;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(4) {
    --icon-index: 3;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(5) {
    --icon-index: 4;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(6) {
    --icon-index: 5;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(7) {
    --icon-index: 6;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(8) {
    --icon-index: 7;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(9) {
    --icon-index: 8;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(10) {
    --icon-index: 9;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(11) {
    --icon-index: 10;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(12) {
    --icon-index: 11;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(13) {
    --icon-index: 12;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(14) {
    --icon-index: 13;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(15) {
    --icon-index: 14;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(16) {
    --icon-index: 15;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(17) {
    --icon-index: 16;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(18) {
    --icon-index: 17;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(19) {
    --icon-index: 18;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(20) {
    --icon-index: 19;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(21) {
    --icon-index: 20;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(22) {
    --icon-index: 21;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(23) {
    --icon-index: 22;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(24) {
    --icon-index: 23;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(25) {
    --icon-index: 24;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(26) {
    --icon-index: 25;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(27) {
    --icon-index: 26;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(28) {
    --icon-index: 27;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(29) {
    --icon-index: 28;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(30) {
    --icon-index: 29;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(31) {
    --icon-index: 30;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(32) {
    --icon-index: 31;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(33) {
    --icon-index: 32;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(34) {
    --icon-index: 33;
    transform: rotate(15deg);
  }
  .icon-pattern i:nth-child(35) {
    --icon-index: 34;
    transform: rotate(-20deg);
  }
  .icon-pattern i:nth-child(36) {
    --icon-index: 35;
    transform: rotate(10deg);
  }
  .icon-pattern i:nth-child(37) {
    --icon-index: 36;
    transform: rotate(-15deg);
  }
  .icon-pattern i:nth-child(38) {
    --icon-index: 37;
    transform: rotate(20deg);
  }
  .icon-pattern i:nth-child(39) {
    --icon-index: 38;
    transform: rotate(-10deg);
  }
  .icon-pattern i:nth-child(40) {
    --icon-index: 39;
    transform: rotate(15deg);
  }

  @keyframes iconFloat {
    0%,
    100% {
      transform: translateY(0px) rotate(var(--rotation, 0deg));
    }
    50% {
      transform: translateY(-20px) rotate(calc(var(--rotation, 0deg) + 10deg));
    }
  }

  .why-section .container {
    position: relative;
    z-index: 2;
  }

  /* Círculos decorativos grandes en los costados */
  .why-section::before {
    content: "";
    position: absolute;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: linear-gradient(
      135deg,
      rgba(255, 255, 255, 0.15) 0%,
      rgba(255, 255, 255, 0.08) 100%
    );
    top: -200px;
    left: -250px;
    z-index: 0;
    box-shadow: 0 0 150px rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .why-section::after {
    content: "";
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: linear-gradient(
      135deg,
      rgba(255, 255, 255, 0.12) 0%,
      rgba(255, 255, 255, 0.06) 100%
    );
    bottom: -300px;
    right: -300px;
    z-index: 0;
    box-shadow: 0 0 180px rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }

  .why-section .container {
    position: relative;
    z-index: 2;
  }

  .why-section h2 {
    font-size: 64px;
    margin-bottom: 20px;
    color: white;
    font-weight: 900;
    text-shadow: 0 6px 30px rgba(0, 0, 0, 0.3);
    letter-spacing: -2px;
    line-height: 1.1;
  }

  .why-subtitle {
    text-align: center;
    font-size: 28px;
    color: rgba(255, 255, 255, 1);
    margin-bottom: 60px;
    font-weight: 600;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    letter-spacing: 0.5px;
  }

  /* GRID ZIGZAG */
  .features-grid-zigzag {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    max-width: 1500px;
    margin: 0 auto;
    padding: 0 20px;
  }

  /* FEATURE CARD - DISEÑO LIMPIO Y UNIFORME */
  .feature-card {
    background: white;
    color: var(--gray-900);
    border-radius: 24px;
    box-shadow:
      0 10px 40px rgba(0, 0, 0, 0.2),
      0 0 0 1px rgba(255, 255, 255, 0.1);
    padding: 40px 32px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    border: none;
    min-height: auto;
  }

  .feature-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(
      90deg,
      var(--primary) 0%,
      #ff6b6b 50%,
      var(--primary) 100%
    );
    transform: scaleX(0);
    transition: transform 0.4s ease;
  }

  .feature-card:hover {
    transform: translateY(-12px);
    box-shadow:
      0 20px 60px rgba(0, 0, 0, 0.3),
      0 0 0 1px rgba(255, 255, 255, 0.2);
  }

  .feature-card:hover::before {
    transform: scaleX(1);
  }

  /* ZIGZAG LAYOUT */
  .feature-card.zigzag-left {
    flex-direction: column;
  }

  .feature-card.zigzag-right {
    flex-direction: column;
  }

  /* VISUAL CONTAINER */
  .feature-visual {
    width: 140px;
    height: 140px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
  }

  .feature-card:hover .feature-visual {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
  }

  .lottie-compact {
    width: 120px;
    height: 120px;
  }

  .feature-icon-compact {
    font-size: 48px;
    margin-bottom: 16px;
    line-height: 1;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
  }

  .feature-card h3 {
    font-size: 22px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 12px;
    line-height: 1.3;
  }

  .feature-card p {
    font-size: 15px;
    line-height: 1.6;
    color: var(--gray-600);
    margin: 0;
  }

  /* STATS SECTION */
  .stats-duo {
    background: white;
    padding: 80px 0;
  }

  .stats-duo h2 {
    font-size: 38px;
    margin-bottom: 12px;
  }

  .stats-subtitle {
    font-size: 18px;
    color: var(--gray-700);
    margin-bottom: 60px;
  }

  .stats-grid-duo {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 32px;
    max-width: 1100px;
    margin: 0 auto;
  }

  .stat-duo {
    text-align: center;
    background: var(--bg-gray);
    padding: 32px 24px;
    border-radius: var(--radius-xl);
    border: 2px solid var(--gray-300);
  }

  .stat-icon-duo {
    font-size: 48px;
    margin-bottom: 16px;
  }

  .stat-number-duo {
    font-size: 48px;
    font-weight: 900;
    color: var(--primary);
    margin-bottom: 8px;
  }

  .stat-label-duo {
    font-size: 16px;
    color: var(--gray-700);
    font-weight: 700;
    margin-bottom: 8px;
  }

  .stat-trend {
    font-size: 13px;
    color: var(--primary);
    font-weight: 700;
  }

  /* EMPRESAS QUE CONFÍAN EN NOSOTROS */
  .companies-section {
    background: white;
    padding: 80px 0;
    border-top: 1px solid var(--gray-200);
  }

  .companies-header {
    text-align: center;
    margin-bottom: 60px;
  }

  .companies-title {
    font-size: 42px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 16px;
    line-height: 1.2;
  }

  .companies-subtitle {
    font-size: 18px;
    color: var(--gray-600);
    font-weight: 600;
  }

  .companies-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 32px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
  }

  .company-logo-card {
    background: white;
    border: 2px solid var(--gray-200);
    border-radius: var(--radius-lg);
    padding: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    height: 140px;
  }

  .company-logo-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    border-color: var(--primary);
  }

  .company-logo-img {
    max-width: 100%;
    max-height: 80px;
    width: auto;
    height: auto;
    object-fit: contain;
    transition: all 0.3s ease;
  }

  .company-logo-card:hover .company-logo-img {
    transform: scale(1.1);
  }

  /* TESTIMONIALS */
  .testimonials-duo {
    background: var(--bg-gray);
    padding: 100px 0;
  }

  .testimonials-duo h2 {
    font-size: 42px;
    margin-bottom: 12px;
  }

  .testi-subtitle {
    text-align: center;
    font-size: 18px;
    color: var(--gray-700);
    margin-bottom: 60px;
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 32px;
  }

  .testimonial-duo {
    background: white;
    padding: 32px;
    border-radius: var(--radius-xl);
    border: 3px solid var(--gray-300);
    box-shadow: var(--shadow-md);
    transition: transform 0.2s;
  }

  .testimonial-duo:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
  }

  .testimonial-header {
    display: flex;
    gap: 16px;
    align-items: center;
    margin-bottom: 20px;
  }

  .testi-name {
    font-weight: 800;
    font-size: 18px;
    color: var(--gray-900);
  }

  .testi-uni {
    font-size: 14px;
    color: var(--gray-700);
    font-weight: 600;
  }

  .testi-text {
    font-size: 16px;
    line-height: 1.6;
    color: var(--gray-700);
    margin-bottom: 20px;
    font-style: italic;
  }

  .testi-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--primary-light);
    color: var(--primary);
    padding: 8px 16px;
    border-radius: var(--radius-full);
    font-size: 13px;
    font-weight: 700;
  }

  /* CTA */
  .cta-duo {
    background: white;
    padding: 100px 0;
  }

  .cta-container {
    text-align: center;
    max-width: 700px;
    margin: 0 auto;
  }

  .mascot-cta {
    font-size: 120px;
    margin-bottom: 32px;
    display: inline-block;
  }

  .cta-duo h2 {
    font-size: 42px;
    margin-bottom: 16px;
  }

  .cta-duo p {
    font-size: 22px;
    color: var(--gray-700);
    margin-bottom: 40px;
  }

  /* RESPONSIVE */
  @media (max-width: 1200px) {
    .features-grid-zigzag {
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }

    .feature-card-horizontal {
      grid-column: span 2;
    }
  }

  @media (max-width: 968px) {
    .hero-container {
      grid-template-columns: 1fr;
      gap: 40px;
    }

    .hero-left h1 {
      font-size: 36px;
    }

    .hero-gif {
      width: 300px;
      height: 300px;
    }

    .why-section {
      padding: 50px 16px;
    }

    .why-section h2 {
      font-size: 36px;
    }

    .why-subtitle {
      font-size: 18px;
    }

    /* RESPONSIVE ZIGZAG */
    .features-grid-zigzag {
      grid-template-columns: 1fr;
      gap: 24px;
    }

    .feature-visual {
      width: 120px;
      height: 120px;
    }

    .lottie-compact {
      width: 100px;
      height: 100px;
    }

    .feature-icon-compact {
      font-size: 40px;
      margin-bottom: 12px;
    }

    .feature-card h3 {
      font-size: 20px;
    }

    .feature-card p {
      font-size: 14px;
    }
  }
</style>
