<script>
  import { onMount } from "svelte";

  let empresaName = "";
  let empresaLogo = "";
  let activeTab = "participantes"; // participantes | hackathons | retos

  // Verificar autenticación
  onMount(() => {
    const isAuth = localStorage.getItem("empresaAuth");
    if (!isAuth) {
      window.location.href = "/empresa/login";
      return;
    }
    empresaName = localStorage.getItem("empresaName") || "Empresa";
    empresaLogo = localStorage.getItem("empresaLogo") || "";
  });

  // Base de datos de participantes (hardcoded)
  const participantes = [
    {
      id: 1,
      nombre: "Diego Alonso Rojas Vera",
      edad: 22,
      universidad: "Universidad Nacional de Ingeniería",
      carrera: "Ingeniería de Sistemas",
      email: "diego.rojas@uni.edu.pe",
      telefono: "+51 987 654 321",
      nivel: "Avanzado",
      proyectos: 6,
      xp: 2150,
      skills: ["Python", "Pandas", "Machine Learning", "SQL"],
      foto: "https://ui-avatars.com/api/?name=Diego+Rojas&background=EF4444&color=fff&size=128",
    },
    {
      id: 2,
      nombre: "Sarai Alejandro",
      edad: 21,
      universidad: "Universidad Nacional de Ingeniería",
      carrera: "Ingeniería Industrial",
      email: "sarai.alejandro@uni.edu.pe",
      telefono: "+51 912 345 678",
      nivel: "Intermedio",
      proyectos: 4,
      xp: 1450,
      skills: ["Python", "Data Analysis", "Excel", "Power BI"],
      foto: "/src/avatars/sarai-alejandro.jpeg",
    },
    {
      id: 3,
      nombre: "Marcelo Castro",
      edad: 23,
      universidad: "Pontificia Universidad Católica del Perú",
      carrera: "Ciencia de la Computación",
      email: "marcelo.castro@pucp.edu.pe",
      telefono: "+51 998 765 432",
      nivel: "Avanzado",
      proyectos: 8,
      xp: 3200,
      skills: ["Python", "Deep Learning", "TensorFlow", "Big Data"],
      foto: "/src/avatars/marcelo-castro.png",
    },
    {
      id: 4,
      nombre: "Ana María Torres",
      edad: 20,
      universidad: "Universidad de Lima",
      carrera: "Ingeniería de Sistemas",
      email: "ana.torres@ulima.edu.pe",
      telefono: "+51 945 123 789",
      nivel: "Intermedio",
      proyectos: 3,
      xp: 980,
      skills: ["Python", "Data Visualization", "SQL"],
      foto: "https://ui-avatars.com/api/?name=Ana+Torres&background=10B981&color=fff&size=128",
    },
    {
      id: 5,
      nombre: "Carlos Mendoza",
      edad: 24,
      universidad: "Universidad Nacional Mayor de San Marcos",
      carrera: "Estadística",
      email: "carlos.mendoza@unmsm.edu.pe",
      telefono: "+51 923 456 123",
      nivel: "Avanzado",
      proyectos: 7,
      xp: 2850,
      skills: ["Python", "R", "Statistical Modeling", "Machine Learning"],
      foto: "https://ui-avatars.com/api/?name=Carlos+Mendoza&background=3B82F6&color=fff&size=128",
    },
  ];

  // Hackathons publicados
  let hackathons = [
    {
      id: 1,
      titulo: "BCP Datathon 2024",
      descripcion: "Predicción de riesgo crediticio usando ML",
      premio: "S/ 10,000",
      participantes: 456,
      estado: "Activo",
      fechaInicio: "2024-01-15",
      fechaFin: "2024-02-28",
    },
  ];

  // Retos publicados
  let retos = [
    {
      id: 1,
      titulo: "Sistema de Detección de Fraude",
      descripcion:
        "Crear un modelo de ML para detectar transacciones fraudulentas",
      dificultad: "Avanzado",
      xp: 500,
      estado: "Activo",
    },
  ];

  // Formularios para crear nuevo contenido
  let showNuevoHackathon = false;
  let showNuevoReto = false;

  let nuevoHackathon = {
    titulo: "",
    descripcion: "",
    premio: "",
    fechaInicio: "",
    fechaFin: "",
  };

  let nuevoReto = {
    titulo: "",
    descripcion: "",
    dificultad: "Intermedio",
    xp: 100,
  };

  function cerrarSesion() {
    localStorage.removeItem("empresaAuth");
    localStorage.removeItem("empresaName");
    localStorage.removeItem("empresaLogo");
    window.location.href = "/";
  }

  function crearHackathon() {
    hackathons = [
      ...hackathons,
      {
        id: hackathons.length + 1,
        ...nuevoHackathon,
        participantes: 0,
        estado: "Activo",
      },
    ];
    showNuevoHackathon = false;
    nuevoHackathon = {
      titulo: "",
      descripcion: "",
      premio: "",
      fechaInicio: "",
      fechaFin: "",
    };
  }

  function crearReto() {
    retos = [
      ...retos,
      {
        id: retos.length + 1,
        ...nuevoReto,
        estado: "Activo",
      },
    ];
    showNuevoReto = false;
    nuevoReto = {
      titulo: "",
      descripcion: "",
      dificultad: "Intermedio",
      xp: 100,
    };
  }
</script>

<svelte:head>
  <title>Dashboard Empresas - Wiñay</title>
</svelte:head>

<div class="dashboard-empresa">
  <!-- SIDEBAR -->
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="logo-empresa">
        {#if empresaLogo}
          <img src={empresaLogo} alt={empresaName} class="empresa-logo-img" />
        {:else}
          <div class="empresa-logo-placeholder">🏢</div>
        {/if}
      </div>
      <h3 class="empresa-name">{empresaName}</h3>
    </div>

    <nav class="sidebar-nav">
      <button
        class="nav-item"
        class:active={activeTab === "participantes"}
        on:click={() => (activeTab = "participantes")}
      >
        <span class="nav-icon">👥</span>
        <span>Participantes</span>
        <span class="badge">{participantes.length}</span>
      </button>

      <button
        class="nav-item"
        class:active={activeTab === "hackathons"}
        on:click={() => (activeTab = "hackathons")}
      >
        <span class="nav-icon">🏆</span>
        <span>Hackathons</span>
        <span class="badge">{hackathons.length}</span>
      </button>

      <button
        class="nav-item"
        class:active={activeTab === "retos"}
        on:click={() => (activeTab = "retos")}
      >
        <span class="nav-icon">💻</span>
        <span>Retos</span>
        <span class="badge">{retos.length}</span>
      </button>
    </nav>

    <button class="btn-logout" on:click={cerrarSesion}>
      <span>🚪</span>
      Cerrar Sesión
    </button>
  </div>

  <!-- MAIN CONTENT -->
  <div class="main-content">
    <!-- HEADER -->
    <div class="content-header">
      <h1 class="page-title">
        {#if activeTab === "participantes"}
          Base de Datos de Talentos
        {:else if activeTab === "hackathons"}
          Mis Hackathons
        {:else}
          Mis Retos
        {/if}
      </h1>

      {#if activeTab === "hackathons"}
        <button class="btn-nuevo" on:click={() => (showNuevoHackathon = true)}>
          <span>➕</span>
          Nuevo Hackathon
        </button>
      {:else if activeTab === "retos"}
        <button class="btn-nuevo" on:click={() => (showNuevoReto = true)}>
          <span>➕</span>
          Nuevo Reto
        </button>
      {/if}
    </div>

    <!-- PARTICIPANTES TAB -->
    {#if activeTab === "participantes"}
      <div class="participantes-grid">
        {#each participantes as participante}
          <div class="participante-card">
            <div class="participante-header">
              <img
                src={participante.foto}
                alt={participante.nombre}
                class="participante-foto"
              />
              <div class="participante-info">
                <h3>{participante.nombre}</h3>
                <p class="universidad">{participante.universidad}</p>
                <div
                  class="nivel-badge nivel-{participante.nivel.toLowerCase()}"
                >
                  {participante.nivel}
                </div>
              </div>
            </div>

            <div class="participante-detalles">
              <div class="detalle-row">
                <span class="detalle-label">Edad:</span>
                <span>{participante.edad} años</span>
              </div>
              <div class="detalle-row">
                <span class="detalle-label">Carrera:</span>
                <span>{participante.carrera}</span>
              </div>
              <div class="detalle-row">
                <span class="detalle-label">Email:</span>
                <span class="email">{participante.email}</span>
              </div>
              <div class="detalle-row">
                <span class="detalle-label">Teléfono:</span>
                <span>{participante.telefono}</span>
              </div>
              <div class="detalle-row">
                <span class="detalle-label">Proyectos:</span>
                <span class="stat">{participante.proyectos} completados</span>
              </div>
              <div class="detalle-row">
                <span class="detalle-label">XP:</span>
                <span class="stat">{participante.xp} puntos</span>
              </div>
            </div>

            <div class="participante-skills">
              <p class="skills-label">Habilidades:</p>
              <div class="skills-tags">
                {#each participante.skills as skill}
                  <span class="skill-tag">{skill}</span>
                {/each}
              </div>
            </div>

            <button class="btn-contactar">
              <span>📧</span>
              Contactar
            </button>
          </div>
        {/each}
      </div>
    {/if}

    <!-- HACKATHONS TAB -->
    {#if activeTab === "hackathons"}
      <div class="hackathons-list">
        {#each hackathons as hackathon}
          <div class="hackathon-card">
            <div class="hackathon-header">
              <h3>{hackathon.titulo}</h3>
              <span
                class="estado-badge estado-{hackathon.estado.toLowerCase()}"
              >
                {hackathon.estado}
              </span>
            </div>
            <p class="hackathon-desc">{hackathon.descripcion}</p>
            <div class="hackathon-stats">
              <div class="stat-item">
                <span class="stat-icon">💰</span>
                <span class="stat-value">{hackathon.premio}</span>
              </div>
              <div class="stat-item">
                <span class="stat-icon">👥</span>
                <span class="stat-value"
                  >{hackathon.participantes} participantes</span
                >
              </div>
              <div class="stat-item">
                <span class="stat-icon">📅</span>
                <span class="stat-value"
                  >{hackathon.fechaInicio} - {hackathon.fechaFin}</span
                >
              </div>
            </div>
          </div>
        {/each}
      </div>
    {/if}

    <!-- RETOS TAB -->
    {#if activeTab === "retos"}
      <div class="retos-grid">
        {#each retos as reto}
          <div class="reto-card">
            <div class="reto-header">
              <h3>{reto.titulo}</h3>
              <span
                class="dificultad-badge dificultad-{reto.dificultad.toLowerCase()}"
              >
                {reto.dificultad}
              </span>
            </div>
            <p class="reto-desc">{reto.descripcion}</p>
            <div class="reto-footer">
              <div class="xp-badge">⭐ {reto.xp} XP</div>
              <span class="estado-small">{reto.estado}</span>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>

<!-- MODAL NUEVO HACKATHON -->
{#if showNuevoHackathon}
  <div class="modal-overlay" on:click={() => (showNuevoHackathon = false)}>
    <div class="modal-content" on:click|stopPropagation>
      <h2>Crear Nuevo Hackathon</h2>
      <form on:submit|preventDefault={crearHackathon}>
        <div class="form-group">
          <label>Título</label>
          <input type="text" bind:value={nuevoHackathon.titulo} required />
        </div>
        <div class="form-group">
          <label>Descripción</label>
          <textarea bind:value={nuevoHackathon.descripcion} required></textarea>
        </div>
        <div class="form-group">
          <label>Premio</label>
          <input
            type="text"
            bind:value={nuevoHackathon.premio}
            placeholder="S/ 10,000"
            required
          />
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Fecha Inicio</label>
            <input
              type="date"
              bind:value={nuevoHackathon.fechaInicio}
              required
            />
          </div>
          <div class="form-group">
            <label>Fecha Fin</label>
            <input type="date" bind:value={nuevoHackathon.fechaFin} required />
          </div>
        </div>
        <div class="modal-actions">
          <button
            type="button"
            class="btn-cancel"
            on:click={() => (showNuevoHackathon = false)}
          >
            Cancelar
          </button>
          <button type="submit" class="btn-submit">Crear Hackathon</button>
        </div>
      </form>
    </div>
  </div>
{/if}

<!-- MODAL NUEVO RETO -->
{#if showNuevoReto}
  <div class="modal-overlay" on:click={() => (showNuevoReto = false)}>
    <div class="modal-content" on:click|stopPropagation>
      <h2>Crear Nuevo Reto</h2>
      <form on:submit|preventDefault={crearReto}>
        <div class="form-group">
          <label>Título</label>
          <input type="text" bind:value={nuevoReto.titulo} required />
        </div>
        <div class="form-group">
          <label>Descripción</label>
          <textarea bind:value={nuevoReto.descripcion} required></textarea>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Dificultad</label>
            <select bind:value={nuevoReto.dificultad}>
              <option value="Principiante">Principiante</option>
              <option value="Intermedio">Intermedio</option>
              <option value="Avanzado">Avanzado</option>
            </select>
          </div>
          <div class="form-group">
            <label>XP</label>
            <input
              type="number"
              bind:value={nuevoReto.xp}
              min="50"
              step="50"
              required
            />
          </div>
        </div>
        <div class="modal-actions">
          <button
            type="button"
            class="btn-cancel"
            on:click={() => (showNuevoReto = false)}
          >
            Cancelar
          </button>
          <button type="submit" class="btn-submit">Crear Reto</button>
        </div>
      </form>
    </div>
  </div>
{/if}

<style>
  .dashboard-empresa {
    display: grid;
    grid-template-columns: 280px 1fr;
    min-height: 100vh;
    background: #f8f9fa;
  }

  /* SIDEBAR */
  .sidebar {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    color: white;
    padding: 32px 24px;
    display: flex;
    flex-direction: column;
  }

  .sidebar-header {
    text-align: center;
    margin-bottom: 40px;
    padding-bottom: 24px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .logo-empresa {
    width: 80px;
    height: 80px;
    margin: 0 auto 16px;
    background: white;
    border-radius: 16px;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .empresa-logo-img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }

  .empresa-logo-placeholder {
    font-size: 40px;
  }

  .empresa-name {
    font-size: 16px;
    font-weight: 800;
    margin: 0;
    line-height: 1.3;
  }

  .sidebar-nav {
    flex: 1;
  }

  .nav-item {
    width: 100%;
    padding: 14px 16px;
    background: transparent;
    border: none;
    color: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    font-size: 15px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
  }

  .nav-item:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
  }

  .nav-item.active {
    background: rgba(239, 68, 68, 0.2);
    color: white;
    border-left: 4px solid #ef4444;
  }

  .nav-icon {
    font-size: 20px;
  }

  .badge {
    margin-left: auto;
    background: rgba(255, 255, 255, 0.2);
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 800;
  }

  .btn-logout {
    padding: 14px 16px;
    background: rgba(239, 68, 68, 0.2);
    border: 2px solid rgba(239, 68, 68, 0.3);
    color: #fecaca;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: center;
  }

  .btn-logout:hover {
    background: #ef4444;
    color: white;
    border-color: #ef4444;
  }

  /* MAIN CONTENT */
  .main-content {
    padding: 40px;
    overflow-y: auto;
  }

  .content-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
  }

  .page-title {
    font-size: 32px;
    font-weight: 900;
    color: var(--gray-900);
    margin: 0;
  }

  .btn-nuevo {
    padding: 12px 24px;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  }

  .btn-nuevo:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
  }

  /* PARTICIPANTES */
  .participantes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 24px;
  }

  .participante-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s;
    border: 2px solid transparent;
  }

  .participante-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    border-color: #ef4444;
  }

  .participante-header {
    display: flex;
    gap: 16px;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 2px solid #f3f4f6;
  }

  .participante-foto {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #ef4444;
  }

  .participante-info h3 {
    font-size: 18px;
    font-weight: 800;
    color: var(--gray-900);
    margin: 0 0 6px 0;
  }

  .universidad {
    font-size: 13px;
    color: var(--gray-600);
    margin: 0 0 10px 0;
    font-weight: 600;
  }

  .nivel-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
  }

  .nivel-principiante {
    background: #dbeafe;
    color: #1e40af;
  }

  .nivel-intermedio {
    background: #fef3c7;
    color: #92400e;
  }

  .nivel-avanzado {
    background: #dcfce7;
    color: #166534;
  }

  .participante-detalles {
    margin-bottom: 20px;
  }

  .detalle-row {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    font-size: 14px;
  }

  .detalle-label {
    font-weight: 700;
    color: var(--gray-700);
  }

  .email {
    color: #3b82f6;
    font-size: 13px;
  }

  .stat {
    color: #ef4444;
    font-weight: 700;
  }

  .participante-skills {
    margin-bottom: 20px;
  }

  .skills-label {
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-700);
    margin-bottom: 8px;
  }

  .skills-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .skill-tag {
    background: #f3f4f6;
    color: var(--gray-700);
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
  }

  .btn-contactar {
    width: 100%;
    padding: 12px;
    background: #ef4444;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: all 0.2s;
  }

  .btn-contactar:hover {
    background: #dc2626;
    transform: translateY(-2px);
  }

  /* HACKATHONS */
  .hackathons-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .hackathon-card {
    background: white;
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    border-left: 6px solid #ef4444;
  }

  .hackathon-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }

  .hackathon-header h3 {
    font-size: 22px;
    font-weight: 900;
    color: var(--gray-900);
    margin: 0;
  }

  .estado-badge {
    padding: 6px 16px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
  }

  .estado-activo {
    background: #dcfce7;
    color: #166534;
  }

  .hackathon-desc {
    font-size: 15px;
    color: var(--gray-700);
    margin-bottom: 20px;
    line-height: 1.6;
  }

  .hackathon-stats {
    display: flex;
    gap: 32px;
  }

  .stat-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    font-weight: 600;
    color: var(--gray-700);
  }

  .stat-icon {
    font-size: 18px;
  }

  /* RETOS */
  .retos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
  }

  .reto-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s;
    border: 2px solid transparent;
  }

  .reto-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    border-color: #ef4444;
  }

  .reto-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 12px;
  }

  .reto-header h3 {
    font-size: 18px;
    font-weight: 800;
    color: var(--gray-900);
    margin: 0;
    flex: 1;
  }

  .dificultad-badge {
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
  }

  .dificultad-principiante {
    background: #dbeafe;
    color: #1e40af;
  }

  .dificultad-intermedio {
    background: #fef3c7;
    color: #92400e;
  }

  .dificultad-avanzado {
    background: #fee2e2;
    color: #991b1b;
  }

  .reto-desc {
    font-size: 14px;
    color: var(--gray-600);
    margin-bottom: 16px;
    line-height: 1.6;
  }

  .reto-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .xp-badge {
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
    color: white;
    padding: 6px 14px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 800;
  }

  .estado-small {
    font-size: 12px;
    color: #10b981;
    font-weight: 700;
  }

  /* MODALS */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    padding: 20px;
  }

  .modal-content {
    background: white;
    border-radius: 20px;
    padding: 32px;
    max-width: 600px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
  }

  .modal-content h2 {
    font-size: 26px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 24px;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: block;
    font-weight: 700;
    color: var(--gray-900);
    margin-bottom: 8px;
    font-size: 14px;
  }

  .form-group input,
  .form-group textarea,
  .form-group select {
    width: 100%;
    padding: 12px 16px;
    border: 2px solid var(--gray-300);
    border-radius: 10px;
    font-size: 15px;
    font-family: "Nunito", sans-serif;
    transition: all 0.2s;
  }

  .form-group textarea {
    min-height: 100px;
    resize: vertical;
  }

  .form-group input:focus,
  .form-group textarea:focus,
  .form-group select:focus {
    outline: none;
    border-color: #ef4444;
    box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .modal-actions {
    display: flex;
    gap: 12px;
    justify-content: flex-end;
    margin-top: 28px;
  }

  .btn-cancel {
    padding: 12px 24px;
    background: var(--gray-200);
    color: var(--gray-700);
    border: none;
    border-radius: 10px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }

  .btn-cancel:hover {
    background: var(--gray-300);
  }

  .btn-submit {
    padding: 12px 24px;
    background: #ef4444;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }

  .btn-submit:hover {
    background: #dc2626;
    transform: translateY(-2px);
  }
</style>
