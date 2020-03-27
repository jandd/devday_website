from rest_framework import serializers, viewsets
from rest_framework.relations import HyperlinkedRelatedField, SlugRelatedField
from talk.models import Talk


class SessionSerializer(serializers.ModelSerializer):
    event = SlugRelatedField(slug_field="slug", read_only=True)
    published_speakers = HyperlinkedRelatedField(
        many=True, read_only=True, view_name="speaker-detail"
    )

    class Meta:
        model = Talk
        fields = ["url", "title", "abstract", "published_speakers", "event"]
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Talk.objects.filter(published_speakers__isnull=False).order_by(
        "-event__start_time", "title", "published_speakers__name"
    )
    serializer_class = SessionSerializer
    lookup_field = "slug"

    def get_queryset(self):
        qs = super().get_queryset()
        event_slug = self.request.query_params.get("event", None)
        if event_slug:
            qs = qs.filter(event__slug=event_slug)
        return qs
