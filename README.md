# mkslides-theme
My MkSlides theme

Use this theme with [MkSlides](https://github.com/MartenBE/mkslides) to create slides with a two-column layout and other features.


## Features
- Two-column layout with different alignments and ratios
- Custom width for elements
- Box elements
- Math support
- Fragmented elements
- Auto-animate support

## Usage

`mkslides serve index.md`

## Custom elements

- two-column layout

```
<!-- c -->
left
<!-- | -->
right
<!-- c. -->
```

- two columns with top alignment

```
<!-- ct -->
...
```

- two columns with bottom alignment

```
<!-- cb -->
...
```

- two columns with 2:1 ratio

```
<!-- c21 -->
...
```

- two columns with 1:2 ratio

```
<!-- c12 -->
...
```

- two columns with 3:1 ratio

```
<!-- c31 -->
...
```

- three columns

```
<!-- c111 -->
...
```

- elements with width

```
![image](image.png)<!-- w100% -->
![image](image.png)<!-- w50% -->
![image](image.png)<!-- w25% -->
```

- box

```
<!-- box -->
text
<!-- . -->

<!-- box --><!-- w50% -->
...
```

- footnote and float

```
<!-- footnote -->
text
<!-- . -->

<!-- footnote --><!-- left -->
...


<!-- footnote --><!-- right -->
...
```

- vertical space

```
<!-- vspace1.5 -->

<!-- vspace3 -->
```

- math

```
<!-- e -->
\nabla \cdot \vec{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \vec{B} &= 0
<!-- e. -->
```

- fragments

```
- item 1 <!-- f0 -->
- item 2 <!-- f1 -->
```

- fit
  
```
# Title <!-- fit -->
```

- auto-animate

```
<!-- anim0 -->
## Title <!-- fit -->
----
<!-- anim -->
## Title 
content
```


