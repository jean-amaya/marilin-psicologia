import streamlit as st
from pathlib import Path
from urllib.parse import quote
import base64

# =====================================================
# CONFIGURACIÓN GENERAL DEL NEGOCIO
# =====================================================
BUSINESS_NAME = "Marilin Amaya"
PROFESSION = "Psicóloga"
BRAND_LINE = "Acompañamiento psicológico para tu bienestar emocional"
PHONE_DISPLAY = "+51 934 386 532"
PHONE_WHATSAPP = "51934386532"
CITY = "Perú"
SCHEDULE = "Lunes a sábado | 9:00 a. m. - 6:00 p. m."
INSTAGRAM_URL = "https://www.instagram.com/"  # Reemplazar por el usuario real del negocio
FACEBOOK_URL = "https://www.facebook.com/"    # Reemplazar por la página real del negocio

ASSETS_DIR = Path(__file__).parent / "assets"
LOGO_PATH = ASSETS_DIR / "logo_marilin_amaya.png"
BANNER_PATH = ASSETS_DIR / "portada_marilin_amaya.png"

WA_TEXT = quote(
    "Hola Marilin, deseo información para agendar una cita de asesoramiento psicológico."
)
WHATSAPP_URL = f"https://wa.me/{PHONE_WHATSAPP}?text={WA_TEXT}"

st.set_page_config(
    page_title=f"{BUSINESS_NAME} | Psicología y Bienestar",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =====================================================
# FUNCIONES DE APOYO
# =====================================================
def image_to_base64(path: Path) -> str:
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

logo_b64 = image_to_base64(LOGO_PATH)

# =====================================================
# ESTILOS CSS
# =====================================================
st.markdown(
    """
    <style>
    :root {
        --bg: #f7f2ec;
        --cream: #fffaf4;
        --sage: #8c9b78;
        --sage-dark: #667356;
        --lilac: #a991b3;
        --gold: #caa24c;
        --text: #3d3935;
        --muted: #756f68;
        --card: rgba(255, 250, 244, 0.86);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(169,145,179,0.15), transparent 32%),
            radial-gradient(circle at bottom right, rgba(140,155,120,0.22), transparent 35%),
            var(--bg);
        color: var(--text);
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 4rem;
        max-width: 1180px;
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(255,250,244,0.96), rgba(244,239,230,0.90));
        border: 1px solid rgba(202,162,76,0.28);
        border-radius: 32px;
        padding: 1.2rem;
        box-shadow: 0 18px 45px rgba(61,57,53,0.08);
        overflow: hidden;
    }

    .hero-banner {
        width: 100%;
        border-radius: 24px;
        display: block;
        border: 1px solid rgba(140,155,120,0.16);
    }

    .hero-content {
        display: grid;
        grid-template-columns: 170px 1fr;
        gap: 1.5rem;
        align-items: center;
        padding: 1.4rem 1rem 0.7rem 1rem;
    }

    .logo-round {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 999px;
        border: 5px solid #fffaf4;
        box-shadow: 0 12px 30px rgba(61,57,53,0.14);
        background: white;
    }

    .eyebrow {
        color: var(--sage-dark);
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 0.78rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .hero-title {
        font-size: clamp(2.2rem, 5vw, 4.8rem);
        line-height: 0.98;
        font-weight: 500;
        letter-spacing: 0.08em;
        color: var(--lilac);
        margin: 0;
        font-family: Georgia, 'Times New Roman', serif;
    }

    .hero-subtitle {
        margin-top: 0.45rem;
        font-size: clamp(1.1rem, 2vw, 1.45rem);
        color: var(--sage-dark);
        letter-spacing: 0.25em;
        text-transform: uppercase;
        font-weight: 600;
    }

    .hero-text {
        font-size: 1.1rem;
        color: var(--muted);
        max-width: 720px;
        margin-top: 0.9rem;
        line-height: 1.7;
    }

    .cta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin-top: 1.3rem;
    }

    .btn-primary, .btn-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
        border-radius: 999px;
        padding: 0.86rem 1.35rem;
        font-weight: 700;
        border: 1px solid transparent;
        transition: all 0.2s ease;
    }

    .btn-primary {
        background: var(--sage);
        color: white !important;
        box-shadow: 0 12px 24px rgba(102,115,86,0.22);
    }

    .btn-primary:hover {
        background: var(--sage-dark);
        transform: translateY(-1px);
    }

    .btn-secondary {
        color: var(--sage-dark) !important;
        border-color: rgba(102,115,86,0.26);
        background: rgba(255,255,255,0.58);
    }

    .section-title {
        font-size: clamp(1.7rem, 3vw, 2.35rem);
        margin: 2.4rem 0 0.7rem 0;
        color: var(--text);
        font-weight: 700;
    }

    .section-intro {
        color: var(--muted);
        max-width: 850px;
        line-height: 1.7;
        font-size: 1.03rem;
        margin-bottom: 1.2rem;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .service-card, .info-card, .step-card {
        background: var(--card);
        border: 1px solid rgba(202,162,76,0.18);
        border-radius: 24px;
        padding: 1.2rem;
        box-shadow: 0 14px 30px rgba(61,57,53,0.06);
        height: 100%;
    }

    .service-icon {
        font-size: 1.9rem;
        margin-bottom: 0.5rem;
    }

    .service-card h3, .info-card h3, .step-card h3 {
        margin: 0 0 0.5rem 0;
        color: var(--sage-dark);
        font-size: 1.1rem;
    }

    .service-card p, .info-card p, .step-card p {
        color: var(--muted);
        line-height: 1.6;
        margin: 0;
        font-size: 0.98rem;
    }

    .two-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-top: 1rem;
    }

    .quote-box {
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(140,155,120,0.20), rgba(169,145,179,0.16));
        border: 1px solid rgba(202,162,76,0.18);
        text-align: center;
    }

    .quote-box h2 {
        font-family: Georgia, 'Times New Roman', serif;
        color: var(--lilac);
        font-size: clamp(1.8rem, 4vw, 3rem);
        font-weight: 500;
        margin-bottom: 0.6rem;
    }

    .contact-card {
        margin-top: 2rem;
        background: #fffaf4;
        border-radius: 32px;
        padding: 1.6rem;
        border: 1px solid rgba(202,162,76,0.28);
        box-shadow: 0 18px 45px rgba(61,57,53,0.08);
    }

    .contact-grid {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 1.2rem;
        align-items: center;
    }

    .contact-number {
        font-size: clamp(1.6rem, 3vw, 2.4rem);
        color: var(--sage-dark);
        font-weight: 800;
        margin: 0.4rem 0;
    }

    .notice {
        background: rgba(255,255,255,0.62);
        border-left: 4px solid var(--gold);
        padding: 1rem 1.1rem;
        border-radius: 18px;
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.95rem;
    }

    .footer {
        text-align: center;
        color: var(--muted);
        font-size: 0.9rem;
        margin-top: 2rem;
        padding-bottom: 1rem;
    }

    @media (max-width: 900px) {
        .hero-content, .two-col, .contact-grid {
            grid-template-columns: 1fr;
        }
        .cards-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .logo-round {
            width: 130px;
            height: 130px;
        }
    }

    @media (max-width: 560px) {
        .cards-grid {
            grid-template-columns: 1fr;
        }
        .hero-card, .contact-card {
            border-radius: 22px;
            padding: 0.8rem;
        }
        .hero-content {
            padding: 1rem 0.4rem 0.4rem 0.4rem;
        }
        .hero-subtitle {
            letter-spacing: 0.15em;
        }
        .cta-row a {
            width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# HERO
# =====================================================
st.markdown(
    f"""
    <section class="hero-card">
        <img class="hero-banner" src="data:image/png;base64,{image_to_base64(BANNER_PATH)}" alt="Portada de {BUSINESS_NAME}">
        <div class="hero-content">
            <div>
                <img class="logo-round" src="data:image/png;base64,{logo_b64}" alt="Logo de {BUSINESS_NAME}">
            </div>
            <div>
                <div class="eyebrow">Psicología y bienestar</div>
                <h1 class="hero-title">{BUSINESS_NAME.upper()}</h1>
                <div class="hero-subtitle">{PROFESSION}</div>
                <p class="hero-text">
                    {BRAND_LINE}. Un espacio de orientación profesional, escucha respetuosa y acompañamiento humano para fortalecer tus recursos personales.
                </p>
                <div class="cta-row">
                    <a class="btn-primary" href="{WHATSAPP_URL}" target="_blank">Agendar cita por WhatsApp</a>
                    <a class="btn-secondary" href="#servicios">Ver servicios</a>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# SERVICIOS
# =====================================================
st.markdown('<h2 class="section-title" id="servicios">Servicios de asesoramiento psicológico</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-intro">Atención orientada a promover bienestar emocional, autoconocimiento y estrategias de afrontamiento para la vida diaria. Cada proceso se coordina de forma previa y se desarrolla con confidencialidad y respeto.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cards-grid">
        <div class="service-card">
            <div class="service-icon">🌿</div>
            <h3>Bienestar emocional</h3>
            <p>Orientación para reconocer emociones, ordenar pensamientos y fortalecer el equilibrio personal.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🧘</div>
            <h3>Estrés y ansiedad</h3>
            <p>Acompañamiento para identificar detonantes y aplicar estrategias de manejo cotidiano.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🤍</div>
            <h3>Autoestima</h3>
            <p>Proceso de fortalecimiento personal, seguridad, autovaloración y toma de decisiones.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🤝</div>
            <h3>Relaciones saludables</h3>
            <p>Orientación para mejorar comunicación, límites, vínculos y resolución de conflictos.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# ENFOQUE Y MODALIDAD
# =====================================================
st.markdown('<h2 class="section-title">Enfoque de atención</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="two-col">
        <div class="info-card">
            <h3>Espacio seguro y confidencial</h3>
            <p>La atención se brinda desde una comunicación respetuosa, ética y centrada en la persona. El objetivo es acompañar el proceso, no juzgarlo.</p>
        </div>
        <div class="info-card">
            <h3>Atención previa cita</h3>
            <p>Las sesiones se coordinan por WhatsApp, según disponibilidad horaria. Se puede adaptar la modalidad a las condiciones del servicio.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="quote-box">
        <h2>Escucha. Comprende. Acompaña.</h2>
        <p>Un proceso psicológico puede ayudarte a mirar con mayor claridad lo que sientes, piensas y necesitas.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# PASOS PARA AGENDAR
# =====================================================
st.markdown('<h2 class="section-title">¿Cómo agendar una cita?</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="cards-grid">
        <div class="step-card">
            <h3>1. Escribe por WhatsApp</h3>
            <p>Solicita información sobre disponibilidad, horarios y modalidad de atención.</p>
        </div>
        <div class="step-card">
            <h3>2. Indica tu motivo de consulta</h3>
            <p>Comparte información general y evita enviar datos sensibles por mensajes públicos.</p>
        </div>
        <div class="step-card">
            <h3>3. Coordina fecha y hora</h3>
            <p>Se confirma la cita según disponibilidad y condiciones del servicio.</p>
        </div>
        <div class="step-card">
            <h3>4. Inicia tu proceso</h3>
            <p>Recibe orientación profesional en un espacio de escucha y acompañamiento.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# CONTACTO
# =====================================================
st.markdown(
    f"""
    <section class="contact-card" id="contacto">
        <div class="contact-grid">
            <div>
                <div class="eyebrow">Contacto</div>
                <h2 class="section-title" style="margin-top:0.2rem;">Agenda tu cita</h2>
                <p class="section-intro" style="margin-bottom:0.4rem;">Comunícate directamente por WhatsApp para consultar disponibilidad y recibir información del servicio.</p>
                <p class="contact-number">{PHONE_DISPLAY}</p>
                <p style="color:var(--muted);"><strong>Horario:</strong> {SCHEDULE}<br><strong>Ubicación:</strong> {CITY}</p>
                <div class="cta-row">
                    <a class="btn-primary" href="{WHATSAPP_URL}" target="_blank">Enviar mensaje</a>
                    <a class="btn-secondary" href="{INSTAGRAM_URL}" target="_blank">Instagram</a>
                    <a class="btn-secondary" href="{FACEBOOK_URL}" target="_blank">Facebook</a>
                </div>
            </div>
            <div class="notice">
                <strong>Nota importante:</strong><br>
                Este sitio permite coordinar información y citas. No reemplaza servicios de emergencia. Si existe una situación de riesgo inmediato, acude al centro de emergencia más cercano o comunícate con una línea de ayuda local.
                <br><br>
                <strong>Dato profesional sugerido:</strong><br>
                Agregar N.° de colegiatura y condición de habilitación cuando corresponda.
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="footer">
        © {BUSINESS_NAME} | Psicología y bienestar emocional. Diseño web desarrollado en Python con Streamlit.
    </div>
    """,
    unsafe_allow_html=True,
)
