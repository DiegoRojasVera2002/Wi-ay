<script>
  import { onMount } from "svelte";
  import { getModules } from "$lib/api";
  import { getUser } from "$lib/api";

  let modules = [];
  let loading = true;
  let user = null;

  // User stats
  let userStats = {
    totalXP: 1250,
    currentStreak: 7,
    projectsCompleted: 3,
    score: 85,
  };

  onMount(async () => {
    try {
      user = getUser();
      modules = await getModules();
    } catch (error) {
      console.error("Error loading modules:", error);
    } finally {
      loading = false;
    }
  });

  const moduleIcons = {
    "Data Science": "📊",
    IoT: "🔌",
    "Web Development": "💻",
    Fintech: "💰",
  };

  // Simulate progress with individual project stars
  function getModuleProgress(index) {
    if (index === 0)
      return {
        completed: 3,
        total: 5,
        status: "in-progress",
        stars: [true, true, true, false, false], // 3 completed, 2 not started
      };
    if (index === 1)
      return {
        completed: 1,
        total: 4,
        status: "in-progress",
        stars: [true, false, false, false], // 1 completed, 3 not started
      };
    if (index === 2)
      return {
        completed: 0,
        total: 6,
        status: "not-started",
        stars: [false, false, false, false, false, false],
      };
    return {
      completed: 0,
      total: 4,
      status: "not-started",
      stars: [false, false, false, false],
    };
  }
</script>

<svelte:head>
  <title>Módulos - Wiñay</title>
</svelte:head>

<div class="modules-page-duo">
  <!-- HEADER WITH USER STATS -->
  <div class="header-duo">
    <div class="container">
      <h1>¡Tu ruta de aprendizaje!</h1>
      <p class="subtitle">
        Completa proyectos reales y avanza en tu carrera tech
      </p>

      <!-- User stats bar -->
      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-icon">🎯</div>
          <div class="stat-info">
            <span class="stat-value">{userStats.score}</span>
            <span class="stat-label">Score</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">⚡</div>
          <div class="stat-info">
            <span class="stat-value">{userStats.totalXP}</span>
            <span class="stat-label">XP Total</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">🔥</div>
          <div class="stat-info">
            <span class="stat-value">{userStats.currentStreak}</span>
            <span class="stat-label">Racha</span>
          </div>
        </div>
        <div class="stat-item">
          <div class="stat-icon">✓</div>
          <div class="stat-info">
            <span class="stat-value">{userStats.projectsCompleted}</span>
            <span class="stat-label">Completados</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- MODULES GRID - UDEMY STYLE -->
  <div class="container">
    {#if loading}
      <div class="loading-duo">
        <div class="loading-spinner">🔄</div>
        <p>Cargando módulos...</p>
      </div>
    {:else if modules.length === 0}
      <div class="empty-state-duo">
        <div class="empty-mascot">🌱</div>
        <h3>¡Pronto habrá módulos increíbles!</h3>
        <p>Estamos preparando proyectos reales para ti</p>
      </div>
    {:else}
      <div class="modules-grid">
        {#each modules as module, index}
          {@const progress = getModuleProgress(index)}

          <div class="module-card">
            <!-- Module image/icon header -->
            <div class="module-card-header">
              <div class="module-icon-large">
                {moduleIcons[module.category] || "📚"}
              </div>
              <div class="progress-circle-small">
                <svg width="60" height="60">
                  <circle
                    cx="30"
                    cy="30"
                    r="26"
                    fill="none"
                    stroke="#e5e7eb"
                    stroke-width="4"
                  />
                  <circle
                    cx="30"
                    cy="30"
                    r="26"
                    fill="none"
                    stroke="var(--primary)"
                    stroke-width="4"
                    stroke-dasharray="{(progress.completed / progress.total) *
                      163} 163"
                    transform="rotate(-90 30 30)"
                  />
                </svg>
                <span class="progress-percentage"
                  >{Math.round(
                    (progress.completed / progress.total) * 100
                  )}%</span
                >
              </div>
            </div>

            <!-- Module content -->
            <div class="module-card-body">
              <h3 class="module-card-title">{module.title}</h3>
              <p class="module-card-description">{module.description}</p>

              <!-- Progress info -->
              <div class="module-card-meta">
                <div class="meta-item">
                  <span class="meta-icon">📚</span>
                  <span class="meta-text">{progress.total} proyectos</span>
                </div>
                <div class="meta-item">
                  <span class="meta-icon">✓</span>
                  <span class="meta-text">{progress.completed} completados</span
                  >
                </div>
              </div>

              <!-- Project stars -->
              <div class="module-stars-inline">
                {#each progress.stars as completed}
                  <span class="star-inline">{completed ? "⭐" : "⚪"}</span>
                {/each}
              </div>

              <!-- Action button -->
              <a href="/modules/{module.id}" class="btn-module-card">
                {#if progress.status === "completed"}
                  <span>Revisar Proyectos</span>
                {:else if progress.completed > 0}
                  <span>Continuar Aprendiendo</span>
                {:else}
                  <span>Comenzar Módulo</span>
                {/if}
                <span class="btn-arrow">→</span>
              </a>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>
```

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
    background: white;
    border-bottom: 2px solid var(--gray-200);
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
    margin-bottom: 32px;
  }

  /* USER STATS BAR */
  .stats-bar {
    display: flex;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
    max-width: 800px;
    margin: 0 auto;
  }

  .stat-item {
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--primary-light);
    padding: 16px 24px;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    border: 2px solid var(--primary);
    transition: all 0.2s;
  }

  .stat-item:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }

  .stat-icon {
    font-size: 32px;
  }

  .stat-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .stat-value {
    font-size: 28px;
    font-weight: 900;
    color: var(--primary);
    line-height: 1;
  }

  .stat-label {
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-700);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 2px;
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
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
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

  /* MODULES GRID - UDEMY STYLE */
  .modules-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 24px;
    padding: 40px 0;
  }

  .module-card {
    background: white;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
    border: 2px solid var(--gray-200);
  }

  .module-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    border-color: var(--primary);
  }

  .module-card-header {
    background: linear-gradient(
      135deg,
      var(--primary-light) 0%,
      var(--primary) 100%
    );
    padding: 32px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
  }

  .module-icon-large {
    font-size: 64px;
    filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
  }

  .progress-circle-small {
    position: relative;
    width: 60px;
    height: 60px;
  }

  .progress-circle-small svg {
    transform: rotate(-90deg);
  }

  .progress-percentage {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 14px;
    font-weight: 800;
    color: white;
  }

  .module-card-body {
    padding: 24px;
  }

  .module-card-title {
    font-size: 20px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 12px;
    line-height: 1.3;
  }

  .module-card-description {
    font-size: 14px;
    color: var(--gray-600);
    margin-bottom: 16px;
    line-height: 1.6;
  }

  .module-card-meta {
    display: flex;
    gap: 16px;
    margin-bottom: 16px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--gray-200);
  }

  .meta-item {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .meta-icon {
    font-size: 18px;
  }

  .meta-text {
    font-size: 13px;
    color: var(--gray-700);
    font-weight: 600;
  }

  .module-stars-inline {
    display: flex;
    gap: 6px;
    margin-bottom: 20px;
  }

  .star-inline {
    font-size: 20px;
    opacity: 0.8;
  }

  .btn-module-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 14px 20px;
    background: var(--primary);
    color: white;
    text-decoration: none;
    border-radius: var(--radius-md);
    font-size: 15px;
    font-weight: 700;
    transition: all 0.2s;
    border: none;
    cursor: pointer;
  }

  .btn-module-card:hover {
    background: var(--primary-hover);
    transform: translateX(4px);
  }

  .btn-arrow {
    font-size: 20px;
    transition: transform 0.2s;
  }

  .btn-module-card:hover .btn-arrow {
    transform: translateX(4px);
  }

  /* LOADING & EMPTY STATES */ /* Progress ring */
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

  .badge-not-started {
    background: var(--gray-100);
    color: var(--gray-600);
    border: 2px dashed var(--gray-300);
  }

  .badge-completed {
    background: var(--primary-light);
    color: var(--primary);
  }

  .badge-progress {
    background: var(--primary-light);
    color: var(--primary);
  }

  /* Individual project stars */
  .project-stars {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }

  .project-star {
    font-size: 24px;
    transition: all 0.2s;
    cursor: default;
  }

  .project-star.completed {
    animation: starBounce 2s ease-in-out infinite;
    filter: drop-shadow(0 2px 4px rgba(255, 193, 7, 0.4));
  }

  .project-star.locked {
    opacity: 0.4;
    filter: grayscale(100%);
  }

  .project-star.not-started {
    opacity: 0.3;
  }

  @keyframes starBounce {
    0%,
    100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.15);
    }
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
    0%,
    100% {
      opacity: 1;
      transform: scale(1);
    }
    50% {
      opacity: 0.5;
      transform: scale(0.9);
    }
  }

  /* Mascot at end */
  .path-mascot {
    text-align: center;
    margin-top: 48px;
  }

  .mascot-circle-path {
    width: 100px;
    height: 100px;
    background: linear-gradient(
      135deg,
      var(--primary-light) 0%,
      var(--primary) 100%
    );
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
      font-size: 28px;
    }

    .subtitle {
      font-size: 16px;
    }

    .stats-bar {
      gap: 12px;
      grid-template-columns: repeat(2, 1fr);
    }

    .stat-item {
      padding: 12px 16px;
    }

    .stat-icon {
      font-size: 24px;
    }

    .stat-value {
      font-size: 20px;
    }

    .stat-label {
      font-size: 11px;
    }

    .modules-grid {
      grid-template-columns: 1fr;
      gap: 20px;
      padding: 24px 0;
    }

    .module-card-header {
      padding: 24px 20px;
    }

    .module-icon-large {
      font-size: 52px;
    }

    .module-card-title {
      font-size: 18px;
    }

    .module-card-description {
      font-size: 13px;
    }
  }
</style>
