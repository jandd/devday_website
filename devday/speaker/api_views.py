from rest_framework import serializers, viewsets
from rest_framework.relations import HyperlinkedRelatedField, SlugRelatedField
from speaker.models import PublishedSpeaker


class PublishedSpeakerSerializer(serializers.ModelSerializer):
    event = SlugRelatedField(slug_field="slug", read_only=True)
    talk_set = HyperlinkedRelatedField(
        many=True, view_name="talk-detail", read_only=True, lookup_field="slug"
    )

    class Meta:
        model = PublishedSpeaker
        fields = [
            "url",
            "name",
            "twitter_handle",
            "short_biography",
            "slug",
            "event",
            "portrait",
            "thumbnail",
            "talk_set",
        ]
        extra_kwargs = {"url": {"view_name": "speaker-detail", "lookup_field": "slug"}}


class PublishedSpeakerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublishedSpeakerSerializer
    lookup_field = "slug"

    def get_queryset(self):
        qs = PublishedSpeaker.objects.order_by("name")
        event = self.request.query_params.get("event", None)
        speaker = self.request.query_params.get("speaker", None)
        if event:
            qs = qs.filter(event__slug=event)
        if speaker:
            qs = qs.filter(slug=speaker)
        return qs
