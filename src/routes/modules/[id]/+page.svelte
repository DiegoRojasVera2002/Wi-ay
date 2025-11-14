<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import { getModuleProjects } from "$lib/api";

  let moduleId;
  let projects = [];
  let loading = true;
  let error = null;
  let moduleTitle = "";
  let completedProjects = 1; // Simulado - solo el primero está completado

  // Métricas del módulo
  let moduleStats = {
    xpEarned: 450,
    timeSpent: "12h 30m",
    accuracy: 92,
    streak: 3,
  };

  $: moduleId = $page.params.id;

  onMount(async () => {
    try {
      projects = await getModuleProjects(moduleId);

      // Obtener título del módulo
      const moduleMap = {
        "1": "Data Science para Fintech",
        "2": "IoT y Automatización Industrial",
        "3": "Desarrollo Web para Mercado",
      };
      moduleTitle = moduleMap[moduleId] || "Módulo";

      // Si es el módulo 1 (Data Science para Fintech), agregar proyectos hardcodeados
      if (moduleId === "1" && projects.length < 6) {
        projects = [
          {
            id: 1,
            title: "Segmentación de Clientes",
            description:
              "Analiza un dataset de transacciones para identificar patrones de gasto usando K-Means",
            company_name: "PrestaTech",
            difficulty: "beginner",
            order: 1,
          },
          {
            id: 2,
            title: "Detección de Fraude",
            description:
              "Construye un modelo de IA que detecte transacciones anómalas en tiempo real",
            company_name: "PagoSeguro",
            difficulty: "intermediate",
            order: 2,
          },
          {
            id: 3,
            title: "Sistema de Recomendación de Productos",
            description:
              "Desarrolla un motor de recomendación para productos financieros usando collaborative filtering",
            company_name: "InnovaBank",
            difficulty: "intermediate",
            order: 3,
          },
          {
            id: 4,
            title: "Análisis de Sentimiento en Redes",
            description:
              "Analiza tweets y comentarios para predecir tendencias del mercado financiero usando NLP",
            company_name: "MercadoPe",
            difficulty: "intermediate",
            order: 4,
          },
          {
            id: 5,
            title: "Predicción de Abandono de Clientes",
            description:
              "Crea un modelo de churn prediction para identificar clientes en riesgo de abandonar servicios bancarios",
            company_name: "Interbank",
            difficulty: "advanced",
            order: 5,
          },
          {
            id: 6,
            title: "Credit Scoring con Deep Learning",
            description:
              "Diseña un sistema avanzado de credit scoring usando redes neuronales para evaluar riesgo crediticio",
            company_name: "BCP",
            difficulty: "advanced",
            order: 6,
          },
        ];
      }

      // Añadir estado de desbloqueo a cada proyecto (estilo Duolingo)
      projects = projects.map((project, index) => ({
        ...project,
        isUnlocked: index === 0 || index < completedProjects,
        isCompleted: index < completedProjects,
        // Métricas por proyecto
        xp:
          index === 0
            ? 150
            : index === 1
              ? 200
              : index === 2
                ? 250
                : index === 3
                  ? 300
                  : index === 4
                    ? 400
                    : 500,
        steps:
          index === 0
            ? 5
            : index === 1
              ? 6
              : index === 2
                ? 7
                : index === 3
                  ? 8
                  : index === 4
                    ? 10
                    : 12,
        estimatedTime:
          index === 0
            ? "4-6 horas"
            : index === 1
              ? "6-8 horas"
              : index === 2
                ? "8-10 horas"
                : index === 3
                  ? "10-12 horas"
                  : index === 4
                    ? "12-15 horas"
                    : "15-20 horas",
      }));
    } catch (err) {
      error = "Error cargando los proyectos";
      console.error(err);
    } finally {
      loading = false;
    }
  });

  const difficultyConfig = {
    beginner: { label: "Principiante", color: "#10b981", icon: "🌱" },
    intermediate: { label: "Intermedio", color: "#f59e0b", icon: "⚡" },
    advanced: { label: "Avanzado", color: "#ef4444", icon: "🔥" },
  };

  // Logos de empresas
  const companyLogos = {
    PrestaTech: "/src/logos_empresas/Prestatech.png",
    PagoSeguro: "/src/logos_empresas/Pagoseguro.png",
    AgroData: "/src/logos_empresas/Agrodata.png",
    LogiTrack: "/src/logos_empresas/Logitrack.png",
    InnovaBank: "/src/logos_empresas/Innovabank.png",
    MercadoPe: "/src/logos_empresas/Mercadope.png",
    Interbank: "/src/logos_empresas/interbank.png",
    BCP: "/src/logos_empresas/Bcp.png",
    Hashi: "HA",
    "Ya Vendió": "YV",
    Artificio: "AR",
  };
</script>

<svelte:head>
  <title>{moduleTitle} - Proyectos - Wiñay</title>
</svelte:head>

<div class="projects-path-page">
  <div class="container">
    <div class="back-link">
      <a href="/modules">
        <span class="back-arrow">←</span> Volver a Módulos
      </a>
    </div>

    {#if loading}
      <div class="loading">
        <div class="spinner"></div>
        <p>Cargando tu ruta...</p>
      </div>
    {:else if error}
      <div class="error-message">{error}</div>
    {:else if projects.length === 0}
      <div class="empty-state">
        <div class="empty-icon">🌱</div>
        <h3>¡Pronto habrá proyectos increíbles!</h3>
        <p>Estamos preparando proyectos reales para ti</p>
      </div>
    {:else}
      <!-- HEADER DEL MÓDULO -->
      <div class="path-header">
        <h1>{moduleTitle}</h1>
        <p class="path-subtitle">
          ¡Tu ruta de aprendizaje! Completa proyectos reales y avanza en tu
          carrera tech
        </p>

        <!-- Progress card -->
        <div class="progress-card-path">
          <div class="progress-info">
            <span class="progress-label">Tu Progreso</span>
            <span class="progress-count"
              >{completedProjects}/{projects.length} proyectos</span
            >
          </div>
          <div class="progress-stars-path">
            {#each projects as project}
              {#if project.isCompleted}
                <span class="star-path completed">⭐</span>
              {:else}
                <span class="star-path locked">🔒</span>
              {/if}
            {/each}
          </div>
        </div>
      </div>

      <!-- MODULE STATS -->
      <div class="module-stats-grid">
        <div class="stat-card">
          <div class="stat-icon-large">⚡</div>
          <div class="stat-content">
            <span class="stat-value-large">{moduleStats.xpEarned}</span>
            <span class="stat-label-card">XP Ganados</span>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon-large">⏱️</div>
          <div class="stat-content">
            <span class="stat-value-large">{moduleStats.timeSpent}</span>
            <span class="stat-label-card">Tiempo Invertido</span>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon-large">🎯</div>
          <div class="stat-content">
            <span class="stat-value-large">{moduleStats.accuracy}%</span>
            <span class="stat-label-card">Precisión</span>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon-large">🔥</div>
          <div class="stat-content">
            <span class="stat-value-large">{moduleStats.streak}</span>
            <span class="stat-label-card">Racha de Días</span>
          </div>
        </div>
      </div>

      <!-- LEARNING PATH - ESTILO DUOLINGO -->
      <div class="learning-path-projects">
        <div class="path-container-projects">
          {#each projects as project, index}
            {@const position = index % 2 === 0 ? "left" : "right"}
            {@const difficulty =
              difficultyConfig[project.difficulty] ||
              difficultyConfig["beginner"]}

            <div
              class="path-node-project {position}"
              class:locked={!project.isUnlocked}
            >
              <!-- Connecting line (except for first) -->
              {#if index > 0}
                <div
                  class="path-line-project"
                  class:locked={!project.isUnlocked}
                ></div>
              {/if}
              <!-- Project Node (circular) -->
              <a
                href={project.isUnlocked ? `/projects/${project.id}` : "#"}
                class="project-node-circle"
                class:locked={!project.isUnlocked}
                class:completed={project.isCompleted}
                class:in-progress={project.isUnlocked && !project.isCompleted}
              >
                <!-- Progress ring -->
                <svg class="progress-ring-project" width="140" height="140">
                  <circle
                    class="progress-ring-bg-project"
                    cx="70"
                    cy="70"
                    r="62"
                  />
                  <circle
                    class="progress-ring-fill-project"
                    cx="70"
                    cy="70"
                    r="62"
                    style="stroke-dasharray: {project.isCompleted
                      ? '389 389'
                      : '0 389'};"
                  />
                </svg>

                <!-- Company logo in center -->
                <div class="node-logo" style="background: {difficulty.color};">
                  {#if companyLogos[project.company_name]?.startsWith("/")}
                    <img
                      src={companyLogos[project.company_name]}
                      alt={project.company_name}
                      class="company-logo-img"
                    />
                  {:else}
                    {companyLogos[project.company_name] ||
                      project.company_name.substring(0, 2).toUpperCase()}
                  {/if}
                </div>
                <!-- Status badge -->
                {#if project.isCompleted}
                  <div class="status-badge-circle completed">✓</div>
                {:else if !project.isUnlocked}
                  <div class="status-badge-circle locked">🔒</div>
                {/if}
              </a>

              <!-- Project info -->
              <div class="project-info-path">
                <!-- Company name -->
                <div class="company-badge">
                  <span class="company-label">Propuesto por</span>
                  <span class="company-name-path">{project.company_name}</span>
                </div>

                <!-- Project number and difficulty -->
                <div class="project-meta-path">
                  <span class="project-number-path"
                    >Proyecto {project.order}</span
                  >
                  <div
                    class="difficulty-badge-path"
                    style="background: {difficulty.color};"
                  >
                    <span>{difficulty.icon}</span>
                    <span>{difficulty.label}</span>
                  </div>
                </div>

                <!-- Status badge for locked projects -->
                {#if !project.isUnlocked}
                  <div class="locked-banner">
                    <span class="locked-icon">🔒</span>
                    <span class="locked-text">BLOQUEADO</span>
                  </div>
                {/if}

                <!-- Title and description -->
                <h3 class="project-title-path">{project.title}</h3>
                <p class="project-description-path">{project.description}</p>

                <!-- Project metrics -->
                {#if project.isUnlocked}
                  <div class="project-metrics">
                    <div class="metric-item">
                      <span class="metric-icon">📝</span>
                      <span class="metric-text">{project.steps} pasos</span>
                    </div>
                    <div class="metric-item">
                      <span class="metric-icon">⏰</span>
                      <span class="metric-text">{project.estimatedTime}</span>
                    </div>
                    {#if project.isCompleted}
                      <div class="metric-item success">
                        <span class="metric-icon">✨</span>
                        <span class="metric-text">+{project.xp} XP</span>
                      </div>
                    {/if}
                  </div>
                {/if}

                <!-- Action button -->
                {#if project.isCompleted}
                  <a
                    href="/projects/{project.id}"
                    class="btn-project-path completed"
                  >
                    <span>Revisar Proyecto</span>
                    <span class="btn-arrow-path">→</span>
                  </a>
                {:else if project.isUnlocked}
                  <a href="/projects/{project.id}" class="btn-project-path">
                    <span>Comenzar Proyecto</span>
                    <span class="btn-arrow-path">→</span>
                  </a>
                {:else}
                  <button class="btn-project-path locked-btn" disabled>
                    🔒 Completa el proyecto anterior
                  </button>
                {/if}
              </div>
            </div>

            <!-- Star decoration between nodes -->
            {#if index < projects.length - 1}
              <div class="path-star-deco">⭐</div>
            {/if}
          {/each}

          <!-- Mascot at the end -->
          <div class="path-mascot-end">
            <div class="mascot-circle-end">🎯</div>
            <h3 class="mascot-title">¡Sigue avanzando!</h3>
            <p class="mascot-text">
              Cada proyecto completado desbloquea el siguiente y te acerca más a
              dominar {moduleTitle}
            </p>
          </div>
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  /* PROJECTS PATH PAGE */
  .projects-path-page {
    min-height: 100vh;
    background: var(--bg);
    padding: 32px 0 80px;
  }

  .container {
    max-width: 700px;
    margin: 0 auto;
    padding: 0 24px;
  }

  /* BACK LINK */
  .back-link {
    margin-bottom: 32px;
  }

  .back-link a {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--primary);
    text-decoration: none;
    font-weight: 700;
    font-size: 16px;
    padding: 12px 20px;
    background: white;
    border-radius: var(--radius-full);
    box-shadow: var(--shadow-sm);
    transition: all 0.2s;
  }

  .back-link a:hover {
    transform: translateX(-4px);
    box-shadow: var(--shadow-md);
  }

  .back-arrow {
    font-size: 20px;
  }

  /* LOADING */
  .loading {
    text-align: center;
    padding: 80px 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }

  .spinner {
    width: 48px;
    height: 48px;
    border: 4px solid var(--gray-300);
    border-top-color: var(--primary);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .loading p,
  .error-message {
    color: var(--gray-700);
    font-weight: 600;
    font-size: 18px;
    text-align: center;
    padding: 48px 24px;
    background: white;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
  }

  /* EMPTY STATE */
  .empty-state {
    text-align: center;
    padding: 80px 24px;
    background: white;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
  }

  .empty-icon {
    font-size: 80px;
    margin-bottom: 24px;
    animation: float 3s ease-in-out infinite;
  }

  @keyframes float {
    0%,
    100% {
      transform: translateY(0px);
    }
    50% {
      transform: translateY(-20px);
    }
  }

  .empty-state h3 {
    font-size: 28px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 12px;
  }

  .empty-state p {
    font-size: 18px;
    color: var(--gray-700);
  }

  /* PATH HEADER */
  .path-header {
    text-align: center;
    background: white;
    border-radius: var(--radius-lg);
    padding: 32px 28px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }

  .path-header h1 {
    font-size: 36px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 8px;
    letter-spacing: -0.5px;
  }

  .path-subtitle {
    font-size: 16px;
    color: var(--gray-600);
    font-weight: 500;
    margin-bottom: 24px;
    line-height: 1.5;
  }

  /* MODULE STATS GRID */
  .module-stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 40px;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
  }

  .stat-card {
    background: white;
    border-radius: var(--radius-md);
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    border: 1px solid var(--gray-200);
    transition: all 0.2s;
  }

  .stat-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--primary-light);
  }

  .stat-icon-large {
    font-size: 32px;
    flex-shrink: 0;
    line-height: 1;
  }

  .stat-content {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .stat-value-large {
    font-size: 24px;
    font-weight: 800;
    color: var(--primary);
    line-height: 1.2;
  }

  .stat-label-card {
    font-size: 11px;
    font-weight: 600;
    color: var(--gray-600);
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }

  .path-subtitle {
    font-size: 20px;
    color: var(--gray-700);
    font-weight: 600;
    margin-bottom: 32px;
    line-height: 1.5;
  }

  /* PROGRESS CARD */
  .progress-card-path {
    background: linear-gradient(135deg, #fca5a5 0%, var(--primary) 100%);
    border-radius: var(--radius-md);
    padding: 20px 28px;
    color: white;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
  }

  .progress-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }

  .progress-label {
    font-size: 14px;
    font-weight: 600;
    opacity: 0.95;
  }

  .progress-count {
    font-size: 20px;
    font-weight: 800;
  }

  .progress-stars-path {
    display: flex;
    gap: 8px;
    justify-content: center;
  }

  .star-path {
    font-size: 24px;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
  }

  .star-path.completed {
    animation: starPulse 2s ease-in-out infinite;
  }

  .star-path.locked {
    opacity: 0.6;
  }

  @keyframes starPulse {
    0%,
    100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
  }

  /* LEARNING PATH - DUOLINGO STYLE */
  .learning-path-projects {
    position: relative;
  }

  .path-container-projects {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 32px;
    padding: 40px 0;
  }

  .path-node-project {
    display: flex;
    align-items: center;
    gap: 32px;
    width: 100%;
    position: relative;
    margin-bottom: 0;
  }

  .path-node-project.left {
    flex-direction: row;
  }

  .path-node-project.right {
    flex-direction: row-reverse;
  }

  /* Connecting line */
  .path-line-project {
    position: absolute;
    top: -32px;
    left: 50%;
    transform: translateX(-50%);
    width: 4px;
    height: 32px;
    background: var(--gray-300);
  }

  .path-line-project.locked {
    background: var(--gray-300);
    opacity: 0.5;
  }

  /* PROJECT NODE (CIRCULAR) */
  .project-node-circle {
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

  .project-node-circle:hover:not(.locked) {
    transform: scale(1.1);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
  }

  .project-node-circle:active:not(.locked) {
    transform: scale(1.05);
  }

  .project-node-circle.locked {
    border-color: var(--gray-400);
    background: var(--gray-100);
    cursor: not-allowed;
    opacity: 0.6;
  }

  .project-node-circle.in-progress {
    border-color: var(--primary);
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%,
    100% {
      box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4);
    }
    50% {
      box-shadow: 0 0 0 10px rgba(239, 68, 68, 0);
    }
  }

  .project-node-circle.completed {
    border-color: var(--success);
    background: #d1fae5;
  }

  /* Progress ring for node */
  .progress-ring-project {
    position: absolute;
    top: -4px;
    left: -4px;
    transform: rotate(-90deg);
  }

  .progress-ring-bg-project {
    fill: none;
    stroke: var(--gray-300);
    stroke-width: 4;
  }

  .progress-ring-fill-project {
    fill: none;
    stroke: var(--success);
    stroke-width: 6;
    stroke-linecap: round;
    transition: stroke-dasharray 0.6s ease;
  }

  /* Company logo in node */
  .node-logo {
    width: 80px;
    height: 80px;
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 900;
    color: white;
    box-shadow: var(--shadow-md);
    z-index: 1;
  }

  .company-logo-img {
    width: 70px;
    height: 70px;
    object-fit: contain;
    background: white;
    border-radius: 8px;
    padding: 6px;
  }

  /* Status badge on node */
  .status-badge-circle {
    position: absolute;
    top: -8px;
    right: -8px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 900;
    border: 3px solid white;
    box-shadow: var(--shadow-md);
  }

  .status-badge-circle.completed {
    background: var(--success);
    color: white;
  }

  .status-badge-circle.locked {
    background: var(--gray-500);
    color: white;
  }

  /* PROJECT INFO */
  .project-info-path {
    flex: 1;
    min-width: 0;
  }

  .path-node-project.left .project-info-path {
    text-align: left;
  }

  .path-node-project.right .project-info-path {
    text-align: right;
  }

  /* Company badge */
  .company-badge {
    display: inline-flex;
    flex-direction: column;
    gap: 2px;
    background: var(--gray-100);
    padding: 8px 16px;
    border-radius: var(--radius-md);
    margin-bottom: 12px;
  }

  .company-label {
    font-size: 11px;
    font-weight: 700;
    color: var(--gray-600);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .company-name-path {
    font-size: 16px;
    font-weight: 800;
    color: var(--gray-900);
  }

  /* Project meta */
  .project-meta-path {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
  }

  .path-node-project.right .project-meta-path {
    justify-content: flex-end;
  }

  .project-number-path {
    font-size: 14px;
    font-weight: 700;
    color: var(--primary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .difficulty-badge-path {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: var(--radius-full);
    color: white;
    font-size: 13px;
    font-weight: 700;
  }

  /* Locked banner */
  .locked-banner {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--gray-500);
    color: white;
    padding: 10px 20px;
    border-radius: var(--radius-md);
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
    box-shadow: var(--shadow-sm);
  }

  .locked-icon {
    font-size: 16px;
  }

  .locked-text {
    font-size: 13px;
  }

  .path-node-project.right .locked-banner {
    margin-left: auto;
  }

  /* Title and description */
  .project-title-path {
    font-size: 26px;
    font-weight: 900;
    color: var(--gray-900);
    margin: 0 0 8px 0;
    line-height: 1.3;
  }

  .path-node-project.locked .project-title-path,
  .path-node-project.locked .project-description-path {
    opacity: 0.6;
  }

  .project-description-path {
    font-size: 15px;
    color: var(--gray-700);
    line-height: 1.6;
    margin: 0 0 16px 0;
  }

  /* PROJECT METRICS */
  .project-metrics {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 16px;
  }

  .path-node-project.right .project-metrics {
    justify-content: flex-end;
  }

  .metric-item {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--gray-100);
    padding: 8px 14px;
    border-radius: var(--radius-full);
    font-size: 14px;
    font-weight: 700;
    color: var(--gray-800);
    border: 2px solid var(--gray-200);
  }

  .metric-item.success {
    background: #d1fae5;
    border-color: var(--success);
    color: var(--success);
  }

  .metric-icon {
    font-size: 16px;
  }

  .metric-text {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  /* Action button */
  .btn-project-path {
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 16px 24px;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: var(--radius-md);
    font-size: 16px;
    font-weight: 800;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    cursor: pointer;
    box-shadow: var(--shadow-button);
    border-bottom: 4px solid var(--primary-dark);
    transition: all 0.2s;
  }

  .btn-project-path:hover:not(:disabled) {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }

  .btn-project-path:active:not(:disabled) {
    transform: translateY(2px);
    box-shadow: 0 2px 0 var(--primary-dark);
  }

  .btn-project-path.completed {
    background: var(--success);
    border-bottom-color: #059669;
  }

  .btn-project-path.locked-btn {
    background: var(--gray-700) !important;
    border-bottom-color: var(--gray-800) !important;
    cursor: not-allowed;
    opacity: 1 !important;
    color: #ffffff !important;
    justify-content: center;
    font-weight: 800;
  }

  .btn-project-path.locked-btn:hover {
    background: var(--gray-700) !important;
    transform: none;
    box-shadow: var(--shadow-button);
  }

  .btn-arrow-path {
    font-size: 20px;
    transition: transform 0.2s;
  }

  .btn-project-path:hover:not(:disabled) .btn-arrow-path {
    transform: translateX(4px);
  }

  /* Star decoration */
  .path-star-deco {
    font-size: 32px;
    animation: twinkle 2s ease-in-out infinite;
  }

  @keyframes twinkle {
    0%,
    100% {
      opacity: 1;
      transform: scale(1);
    }
    50% {
      opacity: 0.6;
      transform: scale(0.9);
    }
  }

  /* Mascot at end */
  .path-mascot-end {
    text-align: center;
    margin-top: 48px;
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-radius: var(--radius-lg);
    padding: 48px 32px;
    box-shadow: var(--shadow-md);
  }

  .mascot-circle-end {
    width: 100px;
    height: 100px;
    background: white;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 56px;
    border: 4px solid #f59e0b;
    box-shadow: var(--shadow-lg);
    margin-bottom: 24px;
    animation: float 3s ease-in-out infinite;
  }

  .mascot-title {
    font-size: 28px;
    font-weight: 900;
    color: var(--gray-900);
    margin: 0 0 12px 0;
  }

  .mascot-text {
    font-size: 18px;
    font-weight: 600;
    color: var(--gray-700);
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.5;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .path-header h1 {
      font-size: 28px;
    }

    .path-subtitle {
      font-size: 14px;
    }

    .module-stats-grid {
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }

    .stat-card {
      padding: 12px 16px;
    }

    .stat-icon-large {
      font-size: 28px;
    }

    .stat-value-large {
      font-size: 20px;
    }

    .stat-label-card {
      font-size: 10px;
    }

    .progress-card-path {
      padding: 16px 20px;
    }

    .progress-label {
      font-size: 12px;
    }

    .progress-count {
      font-size: 18px;
    }

    .star-path {
      font-size: 20px;
    }

    .path-node-project {
      flex-direction: column !important;
      text-align: center;
    }

    .path-node-project.right .project-info-path {
      text-align: center;
    }

    .path-node-project .project-meta-path {
      justify-content: center !important;
    }

    .locked-banner {
      margin-left: 0 !important;
    }

    .project-metrics {
      justify-content: center !important;
    }

    .project-node-circle {
      width: 120px;
      height: 120px;
    }

    .progress-ring-project {
      width: 120px;
      height: 120px;
    }

    .node-logo {
      width: 64px;
      height: 64px;
      font-size: 24px;
    }

    .project-title-path {
      font-size: 22px;
    }

    .project-description-path {
      font-size: 14px;
    }

    .mascot-title {
      font-size: 24px;
    }

    .mascot-text {
      font-size: 16px;
    }
  }
</style>
