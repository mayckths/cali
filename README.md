# cali

Sitio estático publicado con GitHub Pages.

## Cómo funciona

- El contenido del sitio vive en la raíz del repositorio (`index.html`).
- `index.html` se genera con `python3 build.py`. Los datos de cada alojamiento están en ese archivo; edítalos ahí y vuelve a ejecutar el script.
- Las fotos de las tarjetas están en `img/`.
- El workflow `.github/workflows/pages.yml` despliega el sitio a GitHub Pages en cada push a `main`.
- El archivo `.nojekyll` desactiva Jekyll para que los archivos se sirvan tal cual.

## Activar GitHub Pages

Si el primer despliegue falla porque Pages no está habilitado:

1. Ve a **Settings → Pages** en el repositorio.
2. En **Build and deployment → Source**, elige **GitHub Actions**.
3. Vuelve a ejecutar el workflow desde la pestaña **Actions**.

El sitio quedará disponible en `https://mayckths.github.io/cali/`.
