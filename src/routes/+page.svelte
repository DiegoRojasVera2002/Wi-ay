<script>
	import { onMount } from 'svelte';
	import lottie from 'lottie-web';

	onMount(() => {
		// Animación 1: Coding
		lottie.loadAnimation({
			container: document.getElementById('lottie-coding'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json' // Coding animation
		});

		// Animación 2: Success/Trophy
		lottie.loadAnimation({
			container: document.getElementById('lottie-trophy'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets9.lottiefiles.com/packages/lf20_touohxv0.json' // Trophy animation
		});

		// Animación 3: Personalized
		lottie.loadAnimation({
			container: document.getElementById('lottie-personalized'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets1.lottiefiles.com/packages/lf20_v1yudlrx.json' // Personalized animation
		});

		// Animación 4: Team/Community
		lottie.loadAnimation({
			container: document.getElementById('lottie-team'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets5.lottiefiles.com/packages/lf20_myejiggj.json' // Team animation
		});

		// Animación 5: Business
		lottie.loadAnimation({
			container: document.getElementById('lottie-business'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets8.lottiefiles.com/packages/lf20_k0M4I3.json' // Business animation
		});

		// Animación 6: Certificate
		lottie.loadAnimation({
			container: document.getElementById('lottie-certificate'),
			renderer: 'svg',
			loop: true,
			autoplay: true,
			path: 'https://assets1.lottiefiles.com/packages/lf20_tll0j4bb.json' // Certificate animation
		});
	});
</script>

<svelte:head>
	<title>Wiñay - La mejor forma de aprender tecnología</title>
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
		</div>
		<div class="hero-right">
			<img src="src/gif/original-2e51736906dcaf4c009f77942f20b59a.gif" alt="Animated image of learning" class="hero-gif">
		</div>
	</div>
</section>

<!-- POR QUÉ WIÑAY - DISEÑO ZIGZAG 2 COLUMNAS -->
<section class="why-section">
	<div class="container">
		<h2 class="text-center">Por qué Wiñay funciona</h2>
		<p class="why-subtitle">Combinamos ciencia del aprendizaje con tecnología de punta</p>

		<!-- GRID 2 COLUMNAS CON ZIGZAG -->
		<div class="features-grid-zigzag">
			<!-- Feature 1: Efectivo (imagen izquierda) -->
			<div class="feature-card zigzag-left">
				<div class="feature-visual">
					<div id="lottie-coding" class="lottie-compact"></div>
				</div>
				<div class="feature-body">
					<div class="feature-icon-compact">📚</div>
					<h3>Efectivo y comprobado</h3>
					<p>Completar proyectos en Wiñay equivale a un semestre universitario completo de aprendizaje práctico.</p>
					<div class="mini-benefits">
						<span class="mini-tag">✅ Basado en proyectos</span>

						<span class="mini-tag">✅ Validación automática</span>
						<span class="mini-tag">✅ Feedback inmediato</span>
					</div>
				</div>
			</div>

			<!-- Feature 2: Personalizado (imagen derecha) -->
			<div class="feature-card zigzag-right">
				<div class="feature-body">
					<div class="feature-icon-compact">🎯</div>
					<h3>Personalizado para ti</h3>
					<p>Proyectos que se adaptan a tu nivel. Aprende a tu propio ritmo, cuando y donde quieras.</p>
					<div class="quick-stats">
						<div class="quick-stat"><strong>15+</strong> Niveles</div>
						<div class="quick-stat"><strong>100%</strong> Tu ritmo</div>
						<div class="quick-stat"><strong>24/7</strong> Disponible</div>
					</div>
				</div>
				<div class="feature-visual">
					<div id="lottie-personalized" class="lottie-compact"></div>
				</div>
			</div>

			<!-- Feature 3: Motivación (imagen izquierda) -->
			<div class="feature-card zigzag-left">
				<div class="feature-visual">
					<div id="lottie-trophy" class="lottie-compact"></div>
				</div>
				<div class="feature-body">
					<div class="feature-icon-compact">🔥</div>
					<h3>Mantén tu motivación</h3>
					<p>Sistema de rachas, logros y recompensas que hace que aprender sea adictivo y divertido.</p>
					<div class="gamification-compact">
						<div class="game-badge">🔥 7 días</div>
						<div class="game-badge">⭐ +15 XP</div>
						<div class="game-badge">🏆 5 logros</div>
					</div>
				</div>
			</div>

			<!-- Feature 4: Certificados (imagen derecha) -->
			<div class="feature-card zigzag-right">
				<div class="feature-body">
					<div class="feature-icon-compact">🎓</div>
					<h3>Certificados avalados</h3>
					<p>Construye un portafolio profesional con certificados validados por empresas reales.</p>
					<div class="cert-badges">
						<div class="cert-mini">📜 Certificado Digital</div>
						<div class="cert-mini">🏢 Avalado por Empresas</div>
					</div>
				</div>
				<div class="feature-visual">
					<div id="lottie-certificate" class="lottie-compact"></div>
				</div>
			</div>

			<!-- Feature 5: Comunidad (imagen izquierda) -->
			<div class="feature-card zigzag-left">
				<div class="feature-visual">
					<div id="lottie-team" class="lottie-compact"></div>
				</div>
				<div class="feature-body">
					<div class="feature-icon-compact">👥</div>
					<h3>Comunidad activa</h3>
					<p>Más de 1,200 estudiantes peruanos aprendiendo juntos. Comparte y crece con otros.</p>
					<div class="community-compact">
						<div class="comm-badge">💬 1,000+ conversaciones</div>
						<div class="comm-badge">🤝 500+ proyectos compartidos</div>
					</div>
				</div>
			</div>

			<!-- Feature 6: Empresas (imagen derecha) -->
			<div class="feature-card zigzag-right">
				<div class="feature-body">
					<div class="feature-icon-compact">💼</div>
					<h3>Conecta con empresas</h3>
					<p>Completa proyectos reales y accede a oportunidades laborales exclusivas.</p>
					<div class="companies-compact">
						<span class="comp-tag">PrestaTech</span>
						<span class="comp-tag">AgroData</span>
						<span class="comp-tag">LogiTrack</span>
						<span class="comp-tag">InnovaBank</span>
					</div>
				</div>
				<div class="feature-visual">
					<div id="lottie-business" class="lottie-compact"></div>
				</div>
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

<!-- TESTIMONIALS -->
<section class="testimonials-duo">
	<div class="container">
		<h2 class="text-center">Lo que dicen nuestros estudiantes</h2>
		<p class="testi-subtitle">Historias reales de éxito</p>
		<div class="testimonials-grid">
			<div class="testimonial-duo">
				<div class="testimonial-header">
					<div class="avatar-large">MG</div>
					<div>
						<div class="testi-name">María González</div>
						<div class="testi-uni">UNMSM</div>
					</div>
				</div>
				<p class="testi-text">"Gracias a Wiñay conseguí mi primera práctica en una startup tech. Los proyectos reales me dieron la experiencia que necesitaba."</p>
				<div class="testi-badge">
					<span>🎓</span> Certificado en Detección de Fraude
				</div>
			</div>

			<div class="testimonial-duo">
				<div class="testimonial-header">
					<div class="avatar-large">CR</div>
					<div>
						<div class="testi-name">Carlos Ruiz</div>
						<div class="testi-uni">PUCP</div>
					</div>
				</div>
				<p class="testi-text">"Aprendí Data Science desde cero. Ahora trabajo como Data Analyst en una fintech. Wiñay cambió mi vida."</p>
				<div class="testi-badge">
					<span>🎓</span> Certificado en Segmentación de Clientes
				</div>
			</div>

			<div class="testimonial-duo">
				<div class="testimonial-header">
					<div class="avatar-large">AT</div>
					<div>
						<div class="testi-name">Ana Torres</div>
						<div class="testi-uni">UNI</div>
					</div>
				</div>
				<p class="testi-text">"Los proyectos de IoT me prepararon para el mercado laboral real. El mejor recurso para estudiantes peruanos."</p>
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
		<div class="mascot-cta float-animation">
			🌱
		</div>
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

	.hero-right {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.hero-gif {
		width: 400px;
		height: 400px;
		object-fit: contain;
		filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.1));
	}







	/* WHY SECTION - ZIGZAG 2 COLUMNAS */
	.why-section {
		background: var(--bg-gray);
		padding: 60px 0;
	}

	.why-section h2 {
		font-size: 38px;
		margin-bottom: 12px;
	}

	.why-subtitle {
		text-align: center;
		font-size: 18px;
		color: var(--gray-700);
		margin-bottom: 40px;
		font-weight: 600;
	}

	/* GRID ZIGZAG */
	.features-grid-zigzag {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 24px;
	}

	/* FEATURE CARD */
	.feature-card {
		background: var(--info);
		color: white;
		border-radius: var(--radius-lg);
		border: 2px solid #0095d9;
		box-shadow: 0 6px 0 #0095d9;
		padding: 24px;
		display: flex;
		gap: 20px;
		align-items: center;
		transition: all 0.3s;
	}

	.feature-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 8px 0 #0095d9;
	}

	/* ZIGZAG LAYOUT */
	.feature-card.zigzag-left {
		flex-direction: row;
	}

	.feature-card.zigzag-right {
		flex-direction: row-reverse;
	}

	/* VISUAL CONTAINER */
	.feature-visual {
		flex-shrink: 0;
		width: 180px;
		height: 180px;
		background: var(--bg-gray);
		border-radius: var(--radius-lg);
		display: flex;
		align-items: center;
		justify-content: center;
		border: 2px solid var(--gray-300);
	}

	.lottie-compact {
		width: 150px;
		height: 150px;
	}

	/* FEATURE BODY */
	.feature-body {
		flex: 1;
		min-width: 0;
	}

	.feature-icon-compact {
		font-size: 36px;
		margin-bottom: 8px;
	}

	.feature-body h3 {
		font-size: 22px;
		font-weight: 800;
		color: white;
		margin-bottom: 8px;
	}

	.feature-body p {
		font-size: 15px;
		line-height: 1.5;
		color: rgba(255, 255, 255, 0.8);
		margin-bottom: 16px;
	}

	/* MINI BENEFITS */
	.mini-benefits {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.mini-tag {
		display: inline-block;
		background: rgba(255, 255, 255, 0.1);
		padding: 6px 12px;
		border-radius: var(--radius-md);
		font-size: 13px;
		font-weight: 700;
		color: white;
		border: 1px solid rgba(255, 255, 255, 0.2);
	}

	/* QUICK STATS */
	.quick-stats {
		display: flex;
		gap: 10px;
	}

	.quick-stat {
		background: rgba(255, 255, 255, 0.1);
		padding: 8px 14px;
		border-radius: var(--radius-md);
		font-size: 13px;
		font-weight: 700;
		color: white;
		text-align: center;
		border: 2px solid rgba(255, 255, 255, 0.2);
	}

	.quick-stat strong {
		display: block;
		font-size: 18px;
		margin-bottom: 2px;
	}

	/* GAMIFICATION COMPACT */
	.gamification-compact {
		display: flex;
		gap: 8px;
		flex-wrap: wrap;
	}

	.game-badge {
		background: rgba(255, 255, 255, 0.1);
		padding: 8px 14px;
		border-radius: var(--radius-full);
		font-size: 14px;
		font-weight: 800;
		color: white;
		border: 2px solid rgba(255, 255, 255, 0.2);
	}

	/* CERT BADGES */
	.cert-badges {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.cert-mini {
		background: rgba(255, 255, 255, 0.1);
		padding: 8px 12px;
		border-radius: var(--radius-md);
		font-size: 13px;
		font-weight: 700;
		color: white;
		border: 1px solid rgba(255, 255, 255, 0.2);
	}

	/* COMMUNITY COMPACT */
	.community-compact {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.comm-badge {
		background: rgba(255, 255, 255, 0.1);
		padding: 8px 12px;
		border-radius: var(--radius-md);
		font-size: 13px;
		font-weight: 700;
		color: white;
		border: 1px solid rgba(255, 255, 255, 0.2);
	}

	/* COMPANIES COMPACT */
	.companies-compact {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.comp-tag {
		background: white;
		padding: 6px 12px;
		border-radius: var(--radius-full);
		font-size: 12px;
		font-weight: 700;
		color: var(--info);
		border: 2px solid var(--gray-300);
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

		/* ZIGZAG RESPONSIVE */
		.features-grid-zigzag {
			grid-template-columns: 1fr;
			gap: 20px;
		}

		.feature-card {
			flex-direction: column !important;
			text-align: center;
		}

		.feature-visual {
			width: 160px;
			height: 160px;
		}

		.lottie-compact {
			width: 130px;
			height: 130px;
		}

		.feature-body h3 {
			font-size: 20px;
		}

		.feature-body p {
			font-size: 14px;
		}

		.quick-stats {
			flex-direction: column;
		}

		.companies-compact {
			justify-content: center;
		}
	}
</style>

