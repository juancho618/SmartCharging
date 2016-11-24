## Sass

Sass (acrónimo de Syntactically Awesome StyleSheets) es una extensión de CSS que añade características muy potentes y elegantes a este lenguaje de estilos. Sass permite el uso de variables, reglas CSS anidadas, mixins, importación de hojas de estilos y muchas otras características, al tiempo que mantiene la compatibilidad con CSS.

Sass permite organizar mejor las hojas de estilos grandes y permite ser mucho más productivo con las hojas de estilos pequeñas.

En definitiva, Sass incluye las siguientes características:

- 100% compatible con CSS3.
- Permite el uso de variables, anidamiento de estilos y mixins.
- Incluye numerosas funciones para manipular con facilidad colores y otros valores.
- Permite el uso de elementos básicos de programación como las directivas de control y las librerías.

![Css](https://blog.mariusschulz.com/content/images/css_shutter.gif "Css")

#### Para empezar

- Hay una extensión para Visual Studio que ayuda a compilar y ver los archivos Sass, 
  se llama [Mindscape Web Workbench](http://www.mindscapehq.com/products/web-workbench).

#### Tener en cuenta

- Si quieres importar un archivo SCSS o Sass pero no quieres que se compile como archivo CSS, utiliza un guión bajo como primer carácter del nombre del archivo. De esta manera, Sass no generará un archivo CSS para esa hoja de estilos, pero podrás utilizarla importándola dentro de otra hoja de estilos. Este tipo de archivos que no se compilan se denominan "hojas de estilos parciales" o simplemente "parciales" (en inglés, "partials").

- Aunque el nombre del archivo tenga un guión bajo, no es necesario indicarlo en la regla @import. Así por ejemplo, si creas un archivo llamado _colors.scss, entonces no se generará un archivo _colors.css. Sin embargo, podrás utilizarlo en tus hojas de estilos con la regla @import "colors";, que importará el archivo _colors.scss.

- Obviamente no puedes tener en un mismo directorio una hoja de estilos normal y una parcial con el mismo nombre. Siguiendo el ejemplo anterior, en el mismo directorio no puedes tener un archivo llamado _colors.scss y otro llamado colors.scss.

#### Tutorial

##### Sintaxis BEM

- `.block` representa el elemento principal.
- `.block__element` representa el elemento o item de esa clase principal.
- `.block--modifier` representa los diferentes estados que puede tener el `.block`

```sass
.media {
  &__img {
    /* (__) es para elementos */
  }

  &--sm { 
    /* (--) es para modificadores*/
  }
}
```

#### Apps

- http://vswebessentials.com/

-----

#### Referencias

- https://blog.mariusschulz.com/2014/11/16/working-with-sass-stylesheets-in-asp-net-mvc-applications-and-visual-studio#setting-up-bundling-and-minification
- http://thesassway.com/beginner/how-to-structure-a-sass-project
- http://thesassway.com/advanced/pure-sass-functions
- https://www.sitepoint.com/structuring-css-class-selectors-with-sass/


