;; ---------- Plantillas ----------
(deftemplate equipo
   (slot id (type SYMBOL))
   (slot navega (allowed-symbols desconocido si no))
   (slot ping_externo (allowed-symbols desconocido ok falla))
   (slot ping_gateway (allowed-symbols desconocido ok falla))
   (slot ip (allowed-symbols desconocido si no))
   (slot led (allowed-symbols desconocido encendido apagado)))

(deftemplate diagnostico
   (slot equipo (type SYMBOL))
   (slot problema (type SYMBOL))
   (slot regla (type SYMBOL)))        ; parte 3: qué regla lo creó

(deftemplate accion
   (slot problema (type SYMBOL))
   (slot texto (type STRING)))

;; ---------- Acciones como datos ----------
(deffacts acciones
   (accion (problema dns)   (texto "Revisar la configuración DNS"))
   (accion (problema cable) (texto "Revisar el cable de red"))
   (accion (problema dhcp)  (texto "Renovar la IP")))

;; ---------- Reglas ----------
(defrule R1-dns
   (equipo (id ?e) (navega no) (ping_externo ok))
   =>
   (assert (diagnostico (equipo ?e) (problema dns) (regla R1-dns))))

(defrule R3-salida-router
   (equipo (id ?e) (navega no) (ping_externo falla) (ping_gateway ok))
   =>
   (assert (diagnostico (equipo ?e) (problema salida-router)
                        (regla R3-salida-router))))

(defrule R5-dhcp-o-cable
   (equipo (id ?e) (ping_gateway falla) (ip no))
   =>
   (assert (diagnostico (equipo ?e) (problema dhcp-o-cable)
                        (regla R5-dhcp-o-cable))))

(defrule R6-cable
   (diagnostico (equipo ?e) (problema dhcp-o-cable))
   (equipo (id ?e) (led apagado))
   =>
   (assert (diagnostico (equipo ?e) (problema cable) (regla R6-cable))))

(defrule R8-dhcp
   (diagnostico (equipo ?e) (problema dhcp-o-cable))
   (equipo (id ?e) (led encendido))
   =>
   (assert (diagnostico (equipo ?e) (problema dhcp) (regla R8-dhcp))))

(defrule R4-avisar-coordinador
   (declare (salience 10))
   (diagnostico (equipo ?e1) (problema salida-router))
   (diagnostico (equipo ?e2&~?e1) (problema salida-router))
   (not (aviso-coordinador))          ; parte 2.1: quitar esta línea
   =>
   (assert (aviso-coordinador))
   (registrar aula "Avisar al coordinador TIC"))

(defrule recomendar
   (diagnostico (equipo ?e) (problema ?p))
   (accion (problema ?p) (texto ?t))
   =>
   (registrar ?e ?t))