import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="META FASHION AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

SOCIA_NOME = "Isabella Monteiro"

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS – Luxury White Mode
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

:root {
    --gold:        #B8972A;
    --gold-light:  #D4AF5A;
    --gold-dim:    #8C6E1E;
    --white:       #FAFAF8;
    --off-white:   #F3F2EF;
    --gray-100:    #EBEBEB;
    --gray-300:    #C8C8C8;
    --gray-500:    #8A8A8A;
    --graphite:    #3A3A3A;
    --black:       #1A1A1A;
    --radius:      12px;
    --shadow:      0 4px 24px rgba(0,0,0,0.07);
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--white) !important;
    font-family: 'Montserrat', sans-serif;
    color: var(--graphite);
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 2.5rem 3rem 4rem 3rem !important; max-width: 1400px; }

[data-testid="stSidebar"] {
    background: var(--black) !important;
    border-right: 1px solid #2A2A2A;
}
[data-testid="stSidebar"] > div { padding: 0 !important; }

[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    display: flex; flex-direction: column; gap: 4px;
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"] {
    background: transparent; border-radius: 8px;
    padding: 10px 16px; cursor: pointer; transition: all 0.2s;
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"]:hover {
    background: rgba(184,151,42,0.1);
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"] > div:last-child {
    color: var(--gray-300) !important;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.82rem; font-weight: 400;
    letter-spacing: 0.12em; text-transform: uppercase;
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"][aria-checked="true"] {
    background: rgba(184,151,42,0.15);
    border-left: 2px solid var(--gold);
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"][aria-checked="true"] > div:last-child {
    color: var(--gold-light) !important; font-weight: 600;
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"] > div:first-child { display: none; }

[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, var(--gold-dim), var(--gold));
    color: var(--black) !important; border: none; border-radius: 6px;
    font-family: 'Montserrat', sans-serif; font-size: 0.72rem;
    font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase;
    width: 100%; padding: 10px; cursor: pointer; transition: opacity 0.2s;
}
[data-testid="stSidebar"] .stButton > button:hover { opacity: 0.85; }

.stButton > button {
    background: var(--black); color: var(--white) !important;
    border: 1px solid var(--graphite); border-radius: 6px;
    font-family: 'Montserrat', sans-serif; font-size: 0.72rem;
    font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase;
    padding: 10px 24px; transition: all 0.25s;
}
.stButton > button:hover {
    background: var(--gold); border-color: var(--gold); color: var(--black) !important;
}

.stTextArea textarea {
    background: var(--off-white) !important;
    border: 1px solid var(--gray-300) !important;
    border-radius: var(--radius) !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.85rem !important; color: var(--graphite) !important; padding: 14px !important;
}
.stTextArea textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(184,151,42,0.15) !important;
}

hr { border: none; border-top: 1px solid var(--gray-100); margin: 2rem 0; }
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--gray-300); border-radius: 4px; }

.section-title {
    font-family:'Cormorant Garamond',serif;
    font-size:2.6rem; font-weight:300; color:#1A1A1A;
    letter-spacing:0.04em; margin-bottom:0.3rem;
}
.section-sub {
    font-family:'Montserrat',sans-serif; font-size:0.78rem;
    color:#8A8A8A; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:2.5rem;
}
.gold-rule {
    width:60px; height:2px;
    background:linear-gradient(90deg,#B8972A,#D4AF5A);
    margin:0.8rem 0 1.8rem 0; border-radius:2px;
}
.lock-banner {
    background:linear-gradient(135deg,#1A1A1A 60%,#2C2416);
    border:1px solid #B8972A; border-radius:16px;
    padding:3rem 2.5rem; text-align:center; margin-top:1rem;
}
.lock-icon { font-size:2.5rem; margin-bottom:1rem; filter:drop-shadow(0 0 8px #B8972A80); }
.lock-title {
    font-family:'Cormorant Garamond',serif; font-size:2.2rem;
    font-weight:300; color:#D4AF5A; margin-bottom:0.5rem; letter-spacing:0.06em;
}
.lock-sub {
    font-family:'Montserrat',sans-serif; font-size:0.78rem;
    color:#8A8A8A; letter-spacing:0.1em; margin-bottom:2rem;
}
.course-card {
    background:#F3F2EF; border-radius:12px; overflow:hidden;
    box-shadow:0 4px 20px rgba(0,0,0,0.06); transition:transform 0.2s;
}
.course-card:hover { transform:translateY(-4px); }
.course-thumb {
    height:160px; display:flex;
    align-items:center; justify-content:center; font-size:3rem;
}
.course-body { padding:1.2rem 1.4rem 1.4rem; }
.course-label {
    font-family:'Montserrat',sans-serif; font-size:0.6rem; font-weight:600;
    letter-spacing:0.18em; text-transform:uppercase; color:#B8972A; margin-bottom:0.4rem;
}
.course-title {
    font-family:'Cormorant Garamond',serif; font-size:1.25rem;
    font-weight:600; color:#1A1A1A; line-height:1.3; margin-bottom:0.6rem;
}
.course-meta { font-family:'Montserrat',sans-serif; font-size:0.68rem; color:#8A8A8A; letter-spacing:0.06em; }

.price-table { width:100%; border-collapse:collapse; font-family:'Montserrat',sans-serif; font-size:0.8rem; }
.price-table th { padding:1.2rem 1rem; border-bottom:2px solid #EBEBEB; text-align:center; font-weight:500; letter-spacing:0.08em; }
.price-table td { padding:0.9rem 1rem; border-bottom:1px solid #F0F0F0; text-align:center; color:#3A3A3A; vertical-align:middle; }
.price-table tr:hover td { background:#FAFAF6; }
.price-table td:first-child { text-align:left; color:#6A6A6A; font-weight:400; letter-spacing:0.04em; }
.th-plan { font-family:'Cormorant Garamond',serif; font-size:1.3rem; font-weight:400; color:#1A1A1A; display:block; margin-bottom:0.2rem; }
.th-price { font-family:'Montserrat',sans-serif; font-size:0.68rem; font-weight:600; color:#B8972A; letter-spacing:0.1em; }
.check { color:#B8972A; font-size:1rem; }
.cross { color:#C8C8C8; font-size:1rem; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:2rem 1.5rem 1rem;">
        <div style="text-align:center; margin-bottom:2.5rem;">
            <div style="
                font-family:'Cormorant Garamond',serif;
                font-size:1.35rem; font-weight:300;
                letter-spacing:0.22em; color:#B8972A;
                text-transform:uppercase; line-height:1.3;
            ">META<br><span style="font-weight:600;">FASHION</span> AI</div>
            <div style="
                width:40px; height:1px;
                background:linear-gradient(90deg,transparent,#B8972A,transparent);
                margin:0.75rem auto;
            "></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    pagina = st.radio(
        "nav",
        ["✦  Dashboard", "◈  Planos", "◇  Sketch", "◉  Vogue", "▷  Runway", "✿  Couture", "◻  Academy"],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div style="border-top:1px solid #2A2A2A; padding:1.5rem 1.5rem 0.5rem; margin-top:1rem;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.5rem;">
            <div style="width:8px;height:8px;border-radius:50%;background:#B8972A;box-shadow:0 0 6px #B8972A;"></div>
            <span style="font-family:'Montserrat',sans-serif;font-size:0.68rem;color:#8A8A8A;letter-spacing:0.12em;text-transform:uppercase;">Status: Trial Gratuito</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.button("✦ Fazer Upgrade")


# ─────────────────────────────────────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────────────────────────────────────

# ── DASHBOARD ────────────────────────────────────────────────────────────────
if pagina == "✦  Dashboard":
    st.markdown(f"""
    <div style="margin-bottom:2.5rem;">
        <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;color:#B8972A;letter-spacing:0.22em;text-transform:uppercase;margin-bottom:0.6rem;">Olá, {SOCIA_NOME}</div>
        <div class="section-title">Bem-vindo ao Futuro<br>da Moda</div>
        <div class="gold-rule"></div>
        <div class="section-sub">Selecione um módulo para começar sua jornada criativa</div>
    </div>
    """, unsafe_allow_html=True)

    planos = [
        {"tag":"Gratuito","tag_bg":"#EBEBEB","tag_color":"#6A6A6A","nome":"Sketch","emoji":"◇",
         "desc":"Crie e refine prompts profissionais para Midjourney. O ponto de partida perfeito para explorar a IA na moda.",
         "bg":"#FAFAF8","border":"1px solid #EBEBEB","shadow":"0 4px 24px rgba(0,0,0,0.07)","dark":False},
        {"tag":"Essencial","tag_bg":"#F0EAD6","tag_color":"#8C6E1E","nome":"Vogue","emoji":"◉",
         "desc":"Editoriais completos com curadoria de IA. Geração de looks, moodboards e direção criativa avançada.",
         "bg":"linear-gradient(135deg,#FFFFF8,#FAF6E8)","border":"1px solid #D4AF5A50","shadow":"0 4px 24px rgba(184,151,42,0.1)","dark":False},
        {"tag":"Profissional","tag_bg":"#1A1A1A","tag_color":"#D4AF5A","nome":"Runway","emoji":"▷",
         "desc":"Desfiles virtuais gerados por IA. Apresente coleções inteiras em vídeo sem uma única modelo física.",
         "bg":"linear-gradient(135deg,#1C1C1C,#2A2A2A)","border":"1px solid #B8972A40","shadow":"0 8px 40px rgba(0,0,0,0.25)","dark":True},
        {"tag":"Elite","tag_bg":"#B8972A","tag_color":"#FAF6E8","nome":"Couture","emoji":"✿",
         "desc":"A experiência definitiva. Pipeline completo de alta-costura digital: sketch → vogue → runway em um só lugar.",
         "bg":"linear-gradient(135deg,#0D0D0D,#1A150A)","border":"2px solid #B8972A","shadow":"0 8px 40px rgba(0,0,0,0.35)","dark":True},
    ]

    cols = st.columns(4, gap="large")
    for i, (col, p) in enumerate(zip(cols, planos)):
        with col:
            tc = "#FAFAF8" if p["dark"] else "#1A1A1A"
            dc = "#A0A0A0" if p["dark"] else "#6A6A6A"
            st.markdown(f"""
            <div style="background:{p['bg']};border:{p['border']};border-radius:16px;
                padding:2rem 1.6rem 1.8rem;box-shadow:{p['shadow']};min-height:320px;
                display:flex;flex-direction:column;">
                <div>
                    <span style="display:inline-block;background:{p['tag_bg']};color:{p['tag_color']};
                        font-family:'Montserrat',sans-serif;font-size:0.6rem;font-weight:600;
                        letter-spacing:0.2em;text-transform:uppercase;padding:4px 12px;
                        border-radius:20px;margin-bottom:1.2rem;">{p['tag']}</span>
                </div>
                <div style="font-size:1.8rem;margin-bottom:0.5rem;">{p['emoji']}</div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:300;
                    color:{tc};margin-bottom:0.8rem;letter-spacing:0.04em;">{p['nome']}</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.75rem;color:{dc};
                    line-height:1.65;flex:1;font-weight:300;">{p['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Acessar", key=f"dash_{i}", use_container_width=True)


# ── PLANOS ────────────────────────────────────────────────────────────────────
elif pagina == "◈  Planos":
    st.markdown("""
    <div class="section-title">Planos & Preços</div>
    <div class="gold-rule"></div>
    <div class="section-sub">Escolha o plano ideal para a sua jornada criativa</div>
    <table class="price-table">
        <thead>
            <tr>
                <th style="text-align:left;color:#8A8A8A;font-size:0.68rem;letter-spacing:0.14em;text-transform:uppercase;">Recursos</th>
                <th><span class="th-plan">Sketch</span><span class="th-price">Gratuito</span></th>
                <th style="background:linear-gradient(180deg,#FFFFF8,#FAF8F0);">
                    <span class="th-plan" style="color:#B8972A;">Vogue</span><span class="th-price">R$ 97/mês</span></th>
                <th><span class="th-plan">Runway</span><span class="th-price">R$ 197/mês</span></th>
                <th style="background:linear-gradient(180deg,#1A1A1A,#141208);border-radius:0 12px 12px 0;">
                    <span class="th-plan" style="color:#D4AF5A;">Couture</span>
                    <span class="th-price" style="color:#B8972A;">R$ 397/mês</span></th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Geração de Prompts IA</td><td>✦ 10/mês</td><td style="background:#FDFCF5;">✦ 100/mês</td><td>✦ 500/mês</td><td style="color:#D4AF5A;background:#111008;">✦ Ilimitado</td></tr>
            <tr><td>Refinamento High Fashion</td><td><span class="check">✓</span></td><td style="background:#FDFCF5;"><span class="check">✓</span></td><td><span class="check">✓</span></td><td style="background:#111008;"><span class="check">✓</span></td></tr>
            <tr><td>Editoriais com Curadoria IA</td><td><span class="cross">✕</span></td><td style="background:#FDFCF5;"><span class="check">✓</span></td><td><span class="check">✓</span></td><td style="background:#111008;"><span class="check">✓</span></td></tr>
            <tr><td>Moodboards Automáticos</td><td><span class="cross">✕</span></td><td style="background:#FDFCF5;"><span class="check">✓</span></td><td><span class="check">✓</span></td><td style="background:#111008;"><span class="check">✓</span></td></tr>
            <tr><td>Vídeos de Desfile Virtual</td><td><span class="cross">✕</span></td><td style="background:#FDFCF5;"><span class="cross">✕</span></td><td><span class="check">✓</span></td><td style="background:#111008;"><span class="check">✓</span></td></tr>
            <tr><td>Upload de Referências de Vídeo</td><td><span class="cross">✕</span></td><td style="background:#FDFCF5;"><span class="cross">✕</span></td><td><span class="check">✓</span></td><td style="background:#111008;"><span class="check">✓</span></td></tr>
            <tr><td>Pipeline Sketch → Runway</td><td><span class="cross">✕</span></td><td style="background:#FDFCF5;"><span class="cross">✕</span></td><td><span class="cross">✕</span></td><td style="background:#111008;"><span class="check" style="color:#D4AF5A;">✓</span></td></tr>
            <tr><td>Acesso à Academy</td><td>Básico</td><td style="background:#FDFCF5;">Completo</td><td>Completo</td><td style="color:#D4AF5A;background:#111008;">VIP + Mentoria</td></tr>
            <tr><td>Suporte</td><td>Comunidade</td><td style="background:#FDFCF5;">Chat 48h</td><td>Chat 24h</td><td style="color:#D4AF5A;background:#111008;">Dedicado</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for col, label in zip(cols, ["Plano Atual", "Assinar Vogue", "Assinar Runway", "Assinar Couture"]):
        with col:
            st.button(label, use_container_width=True)


# ── SKETCH ────────────────────────────────────────────────────────────────────
elif pagina == "◇  Sketch":
    st.markdown("""
    <div class="section-title">Arquiteto de Prompts</div>
    <div class="gold-rule"></div>
    <div class="section-sub">Transforme sua visão em linguagem que a IA entende</div>
    """, unsafe_allow_html=True)

    col_form, col_result = st.columns([1, 1], gap="large")

    with col_form:
        st.markdown("""
        <div style="background:#F3F2EF;border:1px solid #EBEBEB;border-radius:16px;padding:2rem;">
            <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#1A1A1A;margin-bottom:1.5rem;">Sua Visão Criativa</div>
        """, unsafe_allow_html=True)
        st.text_area(
            "Descreva sua peça ou coleção",
            placeholder="Ex: vestido longo de festa com bordados florais em seda, inspirado na Belle Époque, tons de champagne e marfim...",
            height=180,
        )
        st.multiselect(
            "Referências estéticas",
            ["Haute Couture", "Avant-garde", "Minimal Chic", "Dark Romance", "Coastal Luxury", "Retro Glam", "Neo-Victorian"],
            default=["Haute Couture"],
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("✦ Refinar Prompt para High Fashion", use_container_width=True)

    with col_result:
        st.markdown("""
        <div style="background:#0D0D0D;border:1px solid #2A2A2A;border-radius:16px;padding:2rem;min-height:360px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#D4AF5A;">Prompt Refinado</div>
                <span style="font-family:'Montserrat',sans-serif;font-size:0.6rem;color:#B8972A;
                    background:rgba(184,151,42,0.1);border:1px solid #B8972A40;padding:3px 10px;
                    border-radius:20px;letter-spacing:0.12em;text-transform:uppercase;">Midjourney v6</span>
            </div>
            <div style="background:#1A1A1A;border:1px solid #2A2A2A;border-radius:10px;padding:1.4rem;
                font-family:'Courier New',monospace;font-size:0.75rem;color:#A0A0A0;line-height:1.8;">
                <span style="color:#B8972A;">/imagine prompt:</span>
                vogue italia editorial, haute couture evening gown,
                champagne silk charmeuse with hand-embroidered floral appliqués,
                belle époque silhouette, ivory and gold tones,
                soft candlelight studio photography, shallow depth of field,
                shot on Hasselblad 503CW, Helmut Newton lighting style,
                ultra-detailed fabric texture, fashion week backstage atmosphere
                <span style="color:#B8972A;">--ar 9:16 --style raw --stylize 850 --v 6</span>
            </div>
            <div style="margin-top:1.5rem;">
                <div style="font-family:'Montserrat',sans-serif;font-size:0.65rem;color:#4A4A4A;
                    letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.8rem;">Variações geradas</div>
                <div style="display:flex;gap:8px;">
                    <div style="flex:1;height:80px;background:linear-gradient(135deg,#2A2218,#1A1A1A);
                        border-radius:8px;border:1px solid #3A3218;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">✦</div>
                    <div style="flex:1;height:80px;background:linear-gradient(135deg,#2A2218,#1A1A1A);
                        border-radius:8px;border:1px solid #3A3218;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">◈</div>
                    <div style="flex:1;height:80px;background:linear-gradient(135deg,#2A2218,#1A1A1A);
                        border-radius:8px;border:1px solid #3A3218;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">◉</div>
                    <div style="flex:1;height:80px;background:linear-gradient(135deg,#2A2218,#1A1A1A);
                        border-radius:8px;border:1px solid #3A3218;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">✿</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── VOGUE (BLOQUEADA) ─────────────────────────────────────────────────────────
elif pagina == "◉  Vogue":
    st.markdown("""
    <div class="lock-banner">
        <div class="lock-icon">◉</div>
        <div class="lock-title">Vogue — Recurso Premium</div>
        <div class="lock-sub">Editoriais com curadoria IA · Moodboards automáticos · Direção criativa avançada</div>
        <div style="display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;margin-bottom:2rem;">
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">100+</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Estilos Editoriais</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">IA</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Curadoria Automática</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">∞</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Moodboards</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.button("✦ Assinar Agora — Plano Vogue", use_container_width=True)


# ── RUNWAY (BLOQUEADA + preview) ──────────────────────────────────────────────
elif pagina == "▷  Runway":
    st.markdown("""
    <div class="lock-banner">
        <div class="lock-icon">▷</div>
        <div class="lock-title">Runway — Recurso Premium</div>
        <div class="lock-sub">Desfiles virtuais gerados por IA · Upload de referências · Modelos digitais</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#F3F2EF;border:2px dashed #C8C8C8;border-radius:16px;padding:3rem 2rem;text-align:center;position:relative;margin-bottom:1.5rem;">
        <div style="position:absolute;top:12px;right:12px;background:#1A1A1A;color:#B8972A;
            font-family:'Montserrat',sans-serif;font-size:0.6rem;font-weight:600;letter-spacing:0.15em;
            text-transform:uppercase;padding:4px 10px;border-radius:20px;">🔒 Premium</div>
        <div style="font-size:2.5rem;margin-bottom:0.8rem;opacity:0.3;">▷</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;color:#6A6A6A;margin-bottom:0.4rem;">Upload de Vídeo de Referência</div>
        <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;color:#A0A0A0;letter-spacing:0.08em;">
            Arraste seu vídeo de desfile aqui ou clique para selecionar<br>
            <span style="font-size:0.6rem;">MP4, MOV · Máx. 2GB</span>
        </div>
    </div>
    <div style="background:#0D0D0D;border:1px solid #2A2A2A;border-radius:16px;overflow:hidden;margin-bottom:1.5rem;">
        <div style="height:280px;background:linear-gradient(135deg,#0D0D0D,#1A150A);
            display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;">
            <div style="width:70px;height:70px;border-radius:50%;border:1px solid #B8972A40;
                display:flex;align-items:center;justify-content:center;font-size:1.8rem;
                background:rgba(184,151,42,0.05);">▷</div>
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#D4AF5A;margin-bottom:0.3rem;">Vídeo de Desfile — Exemplo</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.65rem;color:#4A4A4A;letter-spacing:0.1em;text-transform:uppercase;">Coleção Primavera 2026 · 02:34</div>
            </div>
        </div>
        <div style="padding:1rem 1.5rem;background:#111008;display:flex;align-items:center;gap:1rem;">
            <div style="font-size:0.7rem;color:#B8972A;font-family:'Montserrat',sans-serif;letter-spacing:0.08em;">▶ PLAY</div>
            <div style="flex:1;height:2px;background:linear-gradient(90deg,#B8972A 30%,#2A2A2A);border-radius:2px;"></div>
            <div style="font-size:0.65rem;color:#4A4A4A;font-family:'Montserrat',sans-serif;letter-spacing:0.06em;">0:47 / 2:34</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.button("✦ Assinar Agora — Plano Runway", use_container_width=True)


# ── COUTURE (BLOQUEADA) ───────────────────────────────────────────────────────
elif pagina == "✿  Couture":
    st.markdown("""
    <div class="lock-banner">
        <div class="lock-icon">✿</div>
        <div class="lock-title">Couture — Recurso Elite</div>
        <div class="lock-sub">Pipeline completo de Alta-Costura Digital · Sketch → Vogue → Runway em um só lugar</div>
        <div style="display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;margin-bottom:2rem;">
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">∞</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Tudo Ilimitado</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">1</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Ecossistema Completo</div>
            </div>
            <div style="text-align:center;">
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#D4AF5A;">VIP</div>
                <div style="font-family:'Montserrat',sans-serif;font-size:0.62rem;color:#5A5A5A;letter-spacing:0.1em;text-transform:uppercase;">Suporte Dedicado</div>
            </div>
        </div>
        <div style="border-top:1px solid #2A2A2A;padding-top:1.5rem;font-family:'Cormorant Garamond',serif;font-size:1rem;color:#4A4A4A;font-style:italic;">
            "Para a criadora que não aceita menos que a perfeição."
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.button("✦ Assinar Agora — Plano Couture Elite", use_container_width=True)


# ── ACADEMY ───────────────────────────────────────────────────────────────────
elif pagina == "◻  Academy":
    st.markdown("""
    <div class="section-title">Meta Fashion Academy</div>
    <div class="gold-rule"></div>
    <div class="section-sub">Domine a inteligência artificial aplicada à moda de luxo</div>
    """, unsafe_allow_html=True)

    cursos = [
        {"emoji":"🎨","bg":"linear-gradient(135deg,#1A150A,#0D0D0D)","label":"Destaque · Mais Vendido",
         "titulo":"Segredos do Midjourney para Moda",
         "desc":"Da ideia ao editorial: técnicas avançadas de prompt engineering para criar imagens que parecem saídas de revistas de moda internacionais.",
         "aulas":"24 aulas","duracao":"6h 30min","nivel":"Intermediário","stars":"★★★★★"},
        {"emoji":"⚡","bg":"linear-gradient(135deg,#0A1A0D,#0D0D0D)","label":"Novo · 2026",
         "titulo":"Edição Express com IA",
         "desc":"Fluxo de trabalho ultrarrápido com Adobe Firefly, Canva IA e ferramentas de retouch para entregar editoriais em horas, não dias.",
         "aulas":"18 aulas","duracao":"4h 45min","nivel":"Iniciante","stars":"★★★★☆"},
        {"emoji":"◈","bg":"linear-gradient(135deg,#0D0A1A,#0D0D0D)","label":"Tendências · Exclusivo",
         "titulo":"Tendências Digitais 2026",
         "desc":"O que as casas de moda mais influentes estão usando em IA, realidade aumentada e digital fashion para redefinir o futuro da indústria.",
         "aulas":"12 aulas","duracao":"3h 20min","nivel":"Avançado","stars":"★★★★★"},
    ]

    cols = st.columns(3, gap="large")
    for col, c in zip(cols, cursos):
        with col:
            st.markdown(f"""
            <div class="course-card">
                <div class="course-thumb" style="background:{c['bg']};">{c['emoji']}</div>
                <div class="course-body">
                    <div class="course-label">{c['label']}</div>
                    <div class="course-title">{c['titulo']}</div>
                    <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;color:#6A6A6A;line-height:1.6;margin-bottom:1rem;font-weight:300;">{c['desc']}</div>
                    <div class="course-meta">{c['aulas']} · {c['duracao']}<br>
                        <span style="color:#B8972A;">{c['stars']}</span> · {c['nivel']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            st.button("Assistir", key=f"c_{c['titulo'][:6]}", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;padding:2rem 0;">
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#1A1A1A;margin-bottom:0.4rem;font-weight:300;">Mais de 40 aulas chegando em breve</div>
        <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;color:#8A8A8A;letter-spacing:0.1em;text-transform:uppercase;">Styling Digital · Brand Identity com IA · Video Fashion para Reels</div>
    </div>
    """, unsafe_allow_html=True)
