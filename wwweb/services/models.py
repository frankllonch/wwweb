from django.db import models

class AdditionalServiceInfo(models.Model):
    service = models.OneToOneField(
        "services.Service", on_delete=models.CASCADE, related_name="additional_info"
    )
    def __str__(self):
        return f"Info for {self.service.title}"  # Ensure no recursion issues
    

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "PRODUCTOS"
        ordering = ["-created"]

    def __str__(self):
        return self.title

