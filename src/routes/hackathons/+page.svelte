<script>
  import { onMount } from "svelte";

  let activeTab = "all"; // all, hackathons, datathons
  let hackathons = [
    {
      id: 1,
      type: "datathon",
      title: "Datathon BCP: Predicción de Morosidad",
      company: "BCP",
      description:
        "Desarrolla modelos de Machine Learning para predecir la probabilidad de morosidad en créditos personales usando datos históricos de clientes",
      prize: "S/ 10,000",
      participants: 456,
      daysLeft: 18,
      difficulty: "Avanzado",
      tags: ["Machine Learning", "Credit Scoring", "Python", "Scikit-learn"],
      startDate: "20 Nov 2025",
      endDate: "08 Dic 2025",
      logo: "/src/logos_empresas/Bcp.png",
      status: "active",
    },
    {
      id: 2,
      type: "datathon",
      title: "Interbank Data Challenge: Detección de Fraude",
      company: "Interbank",
      description:
        "Crea algoritmos de detección de fraude en tiempo real para transacciones bancarias digitales utilizando técnicas de anomaly detection",
      prize: "S/ 8,500",
      participants: 389,
      daysLeft: 14,
      difficulty: "Avanzado",
      tags: ["Fraud Detection", "Deep Learning", "Real-time Analytics"],
      startDate: "18 Nov 2025",
      endDate: "02 Dic 2025",
      logo: "/src/logos_empresas/interbank.png",
      status: "active",
    },
    {
      id: 3,
      type: "hackathon",
      title: "Fintech Challenge 2025",
      company: "PagoSeguro",
      description:
        "Desarrolla una solución innovadora para detectar fraude en transacciones digitales usando IA",
      prize: "S/ 5,000",
      participants: 234,
      daysLeft: 12,
      difficulty: "Avanzado",
      tags: ["IA", "Fintech", "Machine Learning"],
      startDate: "15 Nov 2025",
      endDate: "27 Nov 2025",
      logo: "/src/logos_empresas/Pagoseguro.png",
      status: "active",
    },
    {
      id: 4,
      type: "datathon",
      title: "AgriTech Data Challenge",
      company: "AgroData",
      description:
        "Analiza datos de sensores IoT para predecir el rendimiento de cultivos en la costa peruana",
      prize: "S/ 3,000",
      participants: 156,
      daysLeft: 8,
      difficulty: "Intermedio",
      tags: ["Data Science", "IoT", "Agricultura"],
      startDate: "10 Nov 2025",
      endDate: "18 Nov 2025",
      logo: "/src/logos_empresas/Agrodata.png",
      status: "active",
    },
    {
      id: 5,
      type: "hackathon",
      title: "Smart City Solutions",
      company: "LogiTrack",
      description:
        "Crea una aplicación web para optimizar rutas de transporte público en Lima usando datos abiertos",
      prize: "S/ 4,500",
      participants: 189,
      daysLeft: 5,
      difficulty: "Intermedio",
      tags: ["Web Dev", "Smart Cities", "APIs"],
      startDate: "08 Nov 2025",
      endDate: "13 Nov 2025",
      logo: "/src/logos_empresas/Logitrack.png",
      status: "active",
    },
    {
      id: 6,
      type: "datathon",
      title: "Retail Analytics Datathon",
      company: "InnovaBank",
      description:
        "Construye modelos predictivos para identificar patrones de compra y mejorar el credit scoring",
      prize: "S/ 6,000",
      participants: 312,
      daysLeft: 20,
      difficulty: "Avanzado",
      tags: ["Analytics", "ML", "Retail"],
      startDate: "18 Nov 2025",
      endDate: "08 Dic 2025",
      logo: "/src/logos_empresas/Innovabank.png",
      status: "active",
    },
    {
      id: 7,
      type: "hackathon",
      title: "HealthTech Innovation",
      company: "MediApp",
      description:
        "Desarrolla una plataforma que conecte pacientes con médicos usando telemedicina y IA",
      prize: "S/ 7,000",
      participants: 267,
      daysLeft: 15,
      difficulty: "Avanzado",
      tags: ["HealthTech", "IA", "Web"],
      startDate: "12 Nov 2025",
      endDate: "27 Nov 2025",
      logo: "/src/logos_empresas/Mediapp.png",
      status: "active",
    },
    {
      id: 8,
      type: "datathon",
      title: "E-commerce Optimization",
      company: "MercadoPe",
      description:
        "Optimiza sistemas de recomendación para aumentar conversiones en plataformas de e-commerce",
      prize: "S/ 3,500",
      participants: 198,
      daysLeft: 0,
      difficulty: "Intermedio",
      tags: ["E-commerce", "Recomendación", "Data"],
      startDate: "01 Nov 2025",
      endDate: "10 Nov 2025",
      logo: "/src/logos_empresas/Mercadope.png",
      status: "finished",
    },
  ];

  let filteredHackathons = hackathons;

  function filterHackathons(type) {
    activeTab = type;
    if (type === "all") {
      filteredHackathons = hackathons;
    } else {
      filteredHackathons = hackathons.filter((h) => h.type === type);
    }
  }

  function getDifficultyColor(difficulty) {
    if (difficulty === "Principiante") return "#10b981";
    if (difficulty === "Intermedio") return "#f59e0b";
    return "#ef4444";
  }
</script>

<svelte:head>
  <title>Hackathones - Wiñay</title>
</svelte:head>

<div class="hackathons-page">
  <!-- HEADER -->
  <div class="header-hackathons">
    <div class="container">
      <h1>🏆 Hackathones & Datathones</h1>
      <p class="subtitle">
        Compite con los mejores, gana premios y demuestra tu talento a empresas
        tech
      </p>

      <!-- Stats Bar -->
      <div class="stats-bar-hackathons">
        <div class="stat-card-hackathon">
          <div class="stat-icon-hack">🎯</div>
          <div>
            <div class="stat-value-hack">8</div>
            <div class="stat-label-hack">Activos</div>
          </div>
        </div>
        <div class="stat-card-hackathon">
          <div class="stat-icon-hack">👥</div>
          <div>
            <div class="stat-value-hack">2,201</div>
            <div class="stat-label-hack">Participantes</div>
          </div>
        </div>
        <div class="stat-card-hackathon">
          <div class="stat-icon-hack">💰</div>
          <div>
            <div class="stat-value-hack">S/ 47,500</div>
            <div class="stat-label-hack">En Premios</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- FILTERS -->
  <div class="container">
    <div class="filters-section">
      <button
        class="filter-btn"
        class:active={activeTab === "all"}
        on:click={() => filterHackathons("all")}
      >
        Todos ({hackathons.length})
      </button>
      <button
        class="filter-btn"
        class:active={activeTab === "hackathon"}
        on:click={() => filterHackathons("hackathon")}
      >
        💻 Hackathones ({hackathons.filter((h) => h.type === "hackathon")
          .length})
      </button>
      <button
        class="filter-btn"
        class:active={activeTab === "datathon"}
        on:click={() => filterHackathons("datathon")}
      >
        📊 Datathones ({hackathons.filter((h) => h.type === "datathon").length})
      </button>
    </div>

    <!-- HACKATHONS GRID -->
    <div class="hackathons-grid">
      {#each filteredHackathons as hackathon}
        <div
          class="hackathon-card"
          class:finished={hackathon.status === "finished"}
        >
          <!-- Header -->
          <div class="hackathon-card-header">
            <img
              src={hackathon.logo}
              alt={hackathon.company}
              class="hackathon-logo-large"
            />
            <div
              class="hackathon-badge-type"
              class:datathon={hackathon.type === "datathon"}
            >
              {hackathon.type === "hackathon" ? "💻 Hackathon" : "📊 Datathon"}
            </div>
          </div>

          <!-- Body -->
          <div class="hackathon-card-body">
            <!-- Company -->
            <div class="company-tag">
              <span class="company-icon">🏢</span>
              <span>{hackathon.company}</span>
            </div>

            <!-- Title -->
            <h3 class="hackathon-title">{hackathon.title}</h3>

            <!-- Description -->
            <p class="hackathon-description">{hackathon.description}</p>

            <!-- Tags -->
            <div class="hackathon-tags">
              {#each hackathon.tags as tag}
                <span class="tag">{tag}</span>
              {/each}
            </div>

            <!-- Meta Info -->
            <div class="hackathon-meta">
              <div class="meta-row">
                <span class="meta-label">🏆 Premio:</span>
                <span class="meta-value prize">{hackathon.prize}</span>
              </div>
              <div class="meta-row">
                <span class="meta-label">👥 Participantes:</span>
                <span class="meta-value">{hackathon.participants}</span>
              </div>
              <div class="meta-row">
                <span class="meta-label">📅 Periodo:</span>
                <span class="meta-value-small"
                  >{hackathon.startDate} - {hackathon.endDate}</span
                >
              </div>
              <div class="meta-row">
                <span class="meta-label">📊 Nivel:</span>
                <span
                  class="difficulty-badge"
                  style="background: {getDifficultyColor(
                    hackathon.difficulty
                  )}20; color: {getDifficultyColor(hackathon.difficulty)};"
                >
                  {hackathon.difficulty}
                </span>
              </div>
            </div>

            <!-- Status & Action -->
            {#if hackathon.status === "active"}
              <div class="time-remaining">
                <span class="clock-icon">⏰</span>
                <span class="time-text">
                  {hackathon.daysLeft > 0
                    ? `${hackathon.daysLeft} días restantes`
                    : "¡Último día!"}
                </span>
              </div>
              <button class="btn-participate" disabled>
                <span>Participar Ahora</span>
                <span class="btn-arrow">→</span>
              </button>
            {:else}
              <div class="finished-badge">✓ Finalizado</div>
              <button class="btn-view-results" disabled>
                Ver Resultados
              </button>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  .hackathons-page {
    min-height: calc(100vh - 80px);
    background: var(--bg);
    padding-bottom: 80px;
  }

  /* HEADER */
  .header-hackathons {
    padding: 48px 0 40px;
    text-align: center;
    background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    border-bottom: 2px solid var(--gray-200);
  }

  .header-hackathons h1 {
    font-size: 42px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 12px;
    letter-spacing: -0.5px;
  }

  .subtitle {
    font-size: 18px;
    color: var(--gray-600);
    margin-bottom: 32px;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }

  .stats-bar-hackathons {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .stat-card-hackathon {
    background: white;
    border-radius: var(--radius-lg);
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    border: 2px solid var(--primary-light);
  }

  .stat-icon-hack {
    font-size: 36px;
  }

  .stat-value-hack {
    font-size: 28px;
    font-weight: 900;
    color: var(--primary);
    line-height: 1;
  }

  .stat-label-hack {
    font-size: 13px;
    font-weight: 600;
    color: var(--gray-600);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* FILTERS */
  .filters-section {
    display: flex;
    gap: 12px;
    padding: 32px 0 24px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .filter-btn {
    padding: 12px 24px;
    border-radius: var(--radius-full);
    border: 2px solid var(--gray-300);
    background: white;
    font-size: 15px;
    font-weight: 700;
    color: var(--gray-700);
    cursor: pointer;
    transition: all 0.2s;
  }

  .filter-btn:hover {
    border-color: var(--primary);
    color: var(--primary);
    transform: translateY(-2px);
  }

  .filter-btn.active {
    background: var(--primary);
    border-color: var(--primary);
    color: white;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
  }

  /* HACKATHONS GRID */
  .hackathons-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 24px;
    padding: 24px 0;
  }

  .hackathon-card {
    background: white;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
    border: 2px solid var(--gray-200);
    position: relative;
  }

  .hackathon-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    border-color: var(--primary);
  }

  .hackathon-card.finished {
    opacity: 0.7;
  }

  .hackathon-card-header {
    background: linear-gradient(
      135deg,
      var(--primary-light) 0%,
      var(--primary) 100%
    );
    padding: 32px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .hackathon-logo-large {
    width: 120px;
    height: 120px;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.15));
    background: white;
    border-radius: 12px;
    padding: 12px;
  }

  .hackathon-badge-type {
    background: white;
    color: var(--primary);
    padding: 8px 16px;
    border-radius: var(--radius-full);
    font-size: 13px;
    font-weight: 800;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .hackathon-badge-type.datathon {
    background: #10b981;
    color: white;
  }

  .hackathon-card-body {
    padding: 24px;
  }

  .company-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-gray);
    padding: 6px 12px;
    border-radius: var(--radius-md);
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-700);
    margin-bottom: 16px;
  }

  .company-icon {
    font-size: 16px;
  }

  .hackathon-title {
    font-size: 22px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 12px;
    line-height: 1.3;
  }

  .hackathon-description {
    font-size: 14px;
    color: var(--gray-600);
    line-height: 1.6;
    margin-bottom: 16px;
  }

  .hackathon-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }

  .tag {
    background: var(--primary-light);
    color: var(--primary);
    padding: 4px 12px;
    border-radius: var(--radius-full);
    font-size: 12px;
    font-weight: 700;
  }

  .hackathon-meta {
    background: var(--bg-gray);
    border-radius: var(--radius-md);
    padding: 16px;
    margin-bottom: 20px;
  }

  .meta-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }

  .meta-row:last-child {
    margin-bottom: 0;
  }

  .meta-label {
    font-size: 13px;
    font-weight: 600;
    color: var(--gray-600);
  }

  .meta-value {
    font-size: 14px;
    font-weight: 800;
    color: var(--gray-900);
  }

  .meta-value.prize {
    color: var(--primary);
    font-size: 16px;
  }

  .meta-value-small {
    font-size: 12px;
    font-weight: 600;
    color: var(--gray-700);
  }

  .difficulty-badge {
    padding: 4px 10px;
    border-radius: var(--radius-md);
    font-size: 12px;
    font-weight: 800;
  }

  .time-remaining {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: #fef3c7;
    color: #92400e;
    padding: 12px;
    border-radius: var(--radius-md);
    margin-bottom: 16px;
    font-weight: 700;
    font-size: 14px;
  }

  .clock-icon {
    font-size: 18px;
  }

  .btn-participate {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 16px 20px;
    background: var(--primary);
    color: white;
    text-decoration: none;
    border-radius: var(--radius-md);
    font-size: 16px;
    font-weight: 800;
    transition: all 0.2s;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border: none;
    cursor: pointer;
  }

  .btn-participate:hover:not(:disabled) {
    background: var(--primary-hover);
    transform: scale(1.02);
  }

  .btn-participate:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .btn-arrow {
    font-size: 20px;
    transition: transform 0.2s;
  }

  .btn-participate:hover .btn-arrow {
    transform: translateX(4px);
  }

  .finished-badge {
    background: var(--gray-300);
    color: var(--gray-700);
    padding: 12px;
    border-radius: var(--radius-md);
    text-align: center;
    font-weight: 800;
    margin-bottom: 12px;
  }

  .btn-view-results {
    display: block;
    width: 100%;
    padding: 14px 20px;
    background: white;
    color: var(--gray-700);
    text-decoration: none;
    border-radius: var(--radius-md);
    font-size: 15px;
    font-weight: 700;
    transition: all 0.2s;
    text-align: center;
    border: 2px solid var(--gray-300);
    cursor: pointer;
  }

  .btn-view-results:hover:not(:disabled) {
    border-color: var(--primary);
    color: var(--primary);
  }

  .btn-view-results:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .header-hackathons h1 {
      font-size: 32px;
    }

    .subtitle {
      font-size: 16px;
    }

    .stats-bar-hackathons {
      flex-direction: column;
      align-items: stretch;
    }

    .stat-card-hackathon {
      justify-content: center;
    }

    .hackathons-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
