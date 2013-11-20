from jumpgate.common.dispatcher import Dispatcher


def get_dispatcher(app):
    disp = Dispatcher(app)

    # V2 API - http://api.openstack.org/api-ref-image.html#os-images-2.0

    disp.add_endpoint('v2_schema_image',
                      '/v2/schemas/image')
    disp.add_endpoint('v2_schema_images',
                      '/v2/schemas/images')
    disp.add_endpoint('v2_image', '/v2/images/{image_guid}')
    disp.add_endpoint('v2_images', '/v2/images')
    disp.add_endpoint('v2_images_detail', '/v2/images/detail')
    disp.add_endpoint('v2_image_file', '/v2/images/{image_guid}/file')
    disp.add_endpoint('v2_image_tag', '/v2/images/{image_guid}/tags/{tag}')
    disp.add_endpoint('v2_tenant_image', '/v2/{tenant_id}/images/{image_guid}')
    disp.add_endpoint('v2_tenant_images', '/v2/{tenant_id}/images')
    disp.add_endpoint('v2_tenant_images_detail',
                      '/v2/{tenant_id}/images/detail')

    # V1 API - http://api.openstack.org/api-ref-image.html#os-images-1.0

    disp.add_endpoint('v1_image', '/v1/images/{image_guid}')
    disp.add_endpoint('v1_images', '/v1/images')
    disp.add_endpoint('v1_images_detail', '/v1/images/detail')
    disp.add_endpoint('v1_image_members', '/v1/images/{image_guid}/members')
    disp.add_endpoint('v1_image_owner',
                      '/v1/images/{image_guid}/members/{owner}')
    disp.add_endpoint('v1_shared_image_owner', '/v1/shared-images/{owner}')
    return disp